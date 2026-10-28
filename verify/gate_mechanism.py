#!/usr/bin/env python3
"""
gate_mechanism.py — every result of the gate-mechanism derivation (notes/gate-mechanism.md), recomputed and
checked. The question: can exchanging the momentum graviton X that #11 §7 constructs produce the dark-matter
velocity gate of #11 §8, which #11 tags "[D — mechanism; shape [O]]"? Two derivations answered it, both executed
outside the repository and kept in review/momentum-gravity/:
  - run 3's theory verifier: run3/verify-critic-theory.json, scripts in scripts/verify-critic-theory/ (v1-v7);
  - run 4's blind second derivation: run4/gate-derivation.json (claims C1-C19), scripts in
    scripts/derivation-gate-mechanism/ (gate_tchannel.py, gate_fermion.py, gate_numbers.py, fiber_overlap.py,
    polarization_lorentz.py).
This file ports their computations (it imports none of them) and is self-contained. The ported source is named at
each section. Check names carry the claim id: C1-C19 for run 4, T-numbers, c1 and 'gate-range' for run 3.

    .venv/bin/python verify/gate_mechanism.py

Exit code 1 if any check fails. Anchors come first and are independent of both derivations: CODATA 2018's hbar c
and MeV/c^2 in grams, from the exact SI constants; the on-shell identity p.p' = m^2 - t/2; the Fierz-Pauli
massive spin-2 numerator (transverse and traceless on shell, a projector of rank 5, and equal to the sum over five
explicitly built helicity tensors, at rest and boosted) and the van Dam-Veltman-Zakharov factor 4/3; the Legendre
polynomials (Bonnet recursion, generating function, orthogonality) and the spherical-harmonic addition theorem,
which is why the residue at a spin-J pole is proportional to P_J of the crossed-channel cosine; the closed-form
Legendre expansions of exp(a z) (modified spherical Bessel functions) and 1/(alpha - z) (Neumann's Q_l); Chebyshev's
min-max property, against brute-force minimization; and the zero-range s-wave cross-section 4 pi a^2/(1 + k^2 a^2)
with the optical theorem. Everything after the anchors is a regression check: it reproduces the derivations' own
numbers and algebra and is not independent of them. Section H sets the two derivations side by side wherever both
computed the same quantity.

Inputs: the record's benchmark (#1 s5.1, #11 s8): m_chi c^2 = 70 MeV, v* ~ 120 km/s, mu = m_chi v*/sqrt2 ~ 20 keV.
The two derivations take different primaries. Run 4 takes mu c = 20 keV, so v* = 121.1 km/s and hbar/mu = 9.87 pm;
run 3 takes v* = 120 km/s, so mu c = 19.813 keV and hbar/mu = 9.96 pm. Each is checked in its own convention.
Gate convention (run 4): amplitude exp(-k^2/mu^2) with k = m v_rel/2, i.e. exp(-v^2/v_a^2) with
v_a = sqrt2 v* = 2 mu c/m; cross-section exp(-v^2/v*^2). Amplitude algebra in hbar = c = 1, metric (+,-,-,-).
CODATA 2018 G = 6.67430e-11 is typed in for run 3's alpha_G.

Runtime is about 8 s and peak memory about 135 MB (the sympy contractions of B and the integrals of E dominate).
The record's scripts were rerun once while porting; their outputs matched the stored .out files byte for byte.
"""
import sys
import time
from math import pi, sqrt, exp, log, erf, cos, sin, cosh, sinh
import mpmath as mp
import numpy as np
import sympy as sp

T_START = time.time()
failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)
def close(x, y, rel):
    return abs(x/y - 1) < rel
def sig(x, n):
    """x rounded to n significant figures"""
    return float(f"{x:.{n - 1}e}")

# exact SI constants (2019) and CODATA 2018 G
H_PL = 6.62607015e-34; C = 299792458.0; EV = 1.602176634e-19
HBAR = H_PL/(2*pi)
HBARC = HBAR*C/(1e6*EV)*1e15                     # MeV fm
C_KMS = C/1e3
MEV_G = 1e6*EV/C**2*1e3                          # grams per MeV/c^2
G_N = 6.67430e-11
M_CHI = 70.0                                     # MeV (#1 s5.1)
MU_R4 = 0.020                                    # MeV: run 4's primary, mu c = 20 keV
VSTAR_R3 = 120.0                                 # km/s: run 3's primary
VSTAR_R4 = sqrt(2)*MU_R4/M_CHI*C_KMS             # 121.1 km/s
VA_R4 = sqrt(2)*VSTAR_R4                         # 171.3 km/s
MU_R3 = M_CHI*(VSTAR_R3/C_KMS)/sqrt(2)           # 0.019813 MeV
ETA = np.diag([1.0, -1.0, -1.0, -1.0])


def qmax(c0, c1, c2, a, b):
    """exact max over x in [a, b] of |c0 + c1 x + c2 x^2| (numpy arrays): the endpoints and the clipped vertex"""
    c0, c1, c2 = np.broadcast_arrays(np.asarray(c0, float), np.asarray(c1, float), np.asarray(c2, float))
    with np.errstate(divide='ignore', invalid='ignore'):
        xv = np.where(c2 != 0, -c1/(2*c2), a)
    xv = np.clip(xv, a, b)
    return np.maximum(np.maximum(np.abs(c0 + c1*a + c2*a*a), np.abs(c0 + c1*b + c2*b*b)), np.abs(c0 + c1*xv + c2*xv*xv))

def minimize2(f, lo1, hi1, lo2, hi2, n=401, rounds=7):
    """brute-force minimum of a convex f(u, v) on a box: grid, then zoom around the best point"""
    best = np.inf
    for _ in range(rounds):
        g1, g2 = np.linspace(lo1, hi1, n), np.linspace(lo2, hi2, n)
        V = f(g1[:, None], g2[None, :])
        i, j = np.unravel_index(np.argmin(V), V.shape)
        best = min(best, V[i, j])
        w1, w2 = 4*(hi1 - lo1)/n, 4*(hi2 - lo2)/n
        lo1, hi1, lo2, hi2 = g1[i] - w1, g1[i] + w1, g2[j] - w2, g2[j] + w2
    return best

def fp_tensor(l, M, metric=ETA):
    """Fierz-Pauli numerator P_{mu nu, rho sigma} (lower indices) with G_{mu nu} = eta_{mu nu} - l_mu l_nu/M^2"""
    ll = metric @ l
    Gm = metric - np.outer(ll, ll)/M**2
    return (0.5*(np.einsum('ac,bd->abcd', Gm, Gm) + np.einsum('ad,bc->abcd', Gm, Gm))
            - np.einsum('ab,cd->abcd', Gm, Gm)/3)

def boost(n, rap):
    n = np.asarray(n, float)/np.linalg.norm(n)
    B = np.eye(4)
    ch, sh = np.cosh(rap), np.sinh(rap)
    B[0, 0] = ch
    B[0, 1:] = B[1:, 0] = sh*n
    B[1:, 1:] = np.eye(3) + (ch - 1)*np.outer(n, n)
    return B

def rotation(axis, ang):
    a = np.asarray(axis, float)/np.linalg.norm(axis)
    Kx = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    R = np.eye(4)
    R[1:, 1:] = np.eye(3) + np.sin(ang)*Kx + (1 - np.cos(ang))*Kx @ Kx
    return R


# ======================================================================================================
def section_anchors():
    print("== A. Anchors (independent of both derivations)")
    # ======================================================================================================
    check("CODATA 2018: hbar c = 197.3269804 MeV fm, from the exact h, c and e", close(HBARC, 197.3269804, 1e-9),
          f"{HBARC:.10f}")
    check("CODATA 2018: 1 MeV/c^2 = 1.78266192e-27 g, from the exact e and c", close(MEV_G, 1.78266192e-27, 1e-8),
          f"{MEV_G:.11e}")

    # on-shell kinematics for arbitrary 3-momenta
    m = sp.symbols('m', positive=True)
    a = sp.symbols('a1:4', real=True)
    b = sp.symbols('b1:4', real=True)
    Ea, Eb = sp.sqrt(m**2 + sum(x**2 for x in a)), sp.sqrt(m**2 + sum(x**2 for x in b))
    pdot = Ea*Eb - sum(x*y for x, y in zip(a, b))
    t = (Ea - Eb)**2 - sum((x - y)**2 for x, y in zip(a, b))
    Psq4 = ((Ea + Eb)**2 - sum((x + y)**2 for x, y in zip(a, b)))/4
    check("on shell (p^2 = p'^2 = m^2), for any 3-momenta: p.p' = m^2 - t/2, i.e. -t = 2 m^2 (gamma - 1) with "
          "gamma = p.p'/m^2; and ((p + p')/2)^2 = m^2 - t/4 (sympy)",
          sp.expand(pdot - (m**2 - t/2)) == 0 and sp.expand(Psq4 - (m**2 - t/4)) == 0 and
          sp.expand(-t - 2*m**2*(pdot/m**2 - 1)) == 0)

    # Fierz-Pauli numerator (textbook; e.g. Hinterbichler, Rev. Mod. Phys. 84, 671 (2012) †)
    rng = np.random.default_rng(2026)
    M = 1.3
    v3 = rng.normal(size=3)
    l = np.array([sqrt(M**2 + v3 @ v3), *v3])
    P = fp_tensor(l, M)
    Pmix = np.einsum('ma,nb,abcd->mncd', ETA, ETA, P)            # first pair raised
    trans = np.abs(np.einsum('a,abcd->bcd', l, P)).max()
    trc = np.abs(np.einsum('ab,abcd->cd', ETA, P)).max()
    proj = np.abs(np.einsum('abmn,mncd->abcd', P, Pmix) - P).max()
    rank = np.einsum('mnmn->', Pmix)
    sym = max(np.abs(P - P.transpose(1, 0, 2, 3)).max(), np.abs(P - P.transpose(2, 3, 0, 1)).max())
    loff = np.array([1.1*l[0], *v3])                              # off shell: l^2 != M^2
    trans_off = np.abs(np.einsum('a,abcd->bcd', loff, fp_tensor(loff, M))).max()
    check("Fierz-Pauli numerator 1/2(G G + G G) - 1/3 G G, G = eta - l l/M^2, on shell l^2 = M^2: symmetric, "
          "transverse (l^mu P = 0) and traceless (eta^{mu nu} P = 0), a projector (P.P = P) of rank P^{mn}_{mn} = 5; "
          "off shell it is not transverse", max(trans, trc, proj, sym) < 1e-12 and abs(rank - 5) < 1e-12 and
          trans_off > 0.1, f"{trans:.1e}, {trc:.1e}, {proj:.1e}; rank {rank:.12f}; off shell {trans_off:.2f}")

    # the five helicity tensors (Condon-Shortley), at rest and boosted
    ex, ey, ez = (np.eye(4)[i].astype(complex) for i in (1, 2, 3))
    ep, em, e0 = -(ex + 1j*ey)/sqrt(2), (ex - 1j*ey)/sqrt(2), ez
    o = np.outer
    eps = [o(ep, ep), (o(ep, e0) + o(e0, ep))/sqrt(2), (o(ep, em) + o(em, ep) + 2*o(e0, e0))/sqrt(6),
           (o(em, e0) + o(e0, em))/sqrt(2), o(em, em)]
    lrest = np.array([M, 0.0, 0.0, 0.0])
    Pup = lambda l_: np.einsum('ai,bj,ck,dl,ijkl->abcd', ETA, ETA, ETA, ETA, fp_tensor(l_, M))
    Ssum = sum(np.einsum('ab,cd->abcd', e, e.conj()) for e in eps)
    Lb = boost(rng.normal(size=3), 0.8)
    eps_b = [Lb @ e @ Lb.T for e in eps]
    Ssum_b = sum(np.einsum('ab,cd->abcd', e, e.conj()) for e in eps_b)
    gram = np.array([[np.einsum('ab,ac,bd,cd->', e1.conj(), ETA, ETA, e2) for e2 in eps] for e1 in eps])
    dev_rest, dev_boost = np.abs(Ssum - Pup(lrest)).max(), np.abs(Ssum_b - Pup(Lb @ lrest)).max()
    check("the sum over the five helicity tensors eps(+-2) = e+-e+-, eps(+-1) = (e+-e0 + e0e+-)/sqrt2, "
          "eps(0) = (e+e- + e-e+ + 2e0e0)/sqrt6 equals the Fierz-Pauli numerator, at rest and after a boost; they are "
          "orthonormal", max(dev_rest, dev_boost) < 1e-13 and np.abs(gram - np.eye(5)).max() < 1e-13,
          f"{dev_rest:.1e}, {dev_boost:.1e}")
    av, bv = rng.normal(size=3), rng.normal(size=3)
    A4, B4 = np.array([0, *av]), np.array([0, *bv])
    lhs = sum(np.einsum('a,b,ab->', A4, A4, e)*np.conj(np.einsum('a,b,ab->', B4, B4, e)) for e in eps)
    cosab = av @ bv/np.linalg.norm(av)/np.linalg.norm(bv)
    rhs = 2/3*(av @ av)*(bv @ bv)*(3*cosab**2 - 1)/2
    check("spin-2 residue factorization at rest: sum_lambda (a.eps.a)(b.eps.b)* = (2/3)|a|^2|b|^2 P_2(cos theta_ab)",
          abs(lhs - rhs) < 1e-12*abs(rhs), f"{lhs.real:.12f} vs {rhs:.12f}")

    # vDVZ: static conserved sources, exchange momentum spatial (l^0 = 0, l_mu T^{mu nu} = 0)
    T = np.zeros((4, 4)); T[0, 0] = 1.0
    lst = np.array([0.0, 0.7, 0.0, 0.0])
    fp_st = np.einsum('ab,abcd,cd->', T, fp_tensor(lst, M), T)
    D0 = 0.5*(np.einsum('ac,bd->abcd', ETA, ETA) + np.einsum('ad,bc->abcd', ETA, ETA)) - 0.5*np.einsum('ab,cd->abcd', ETA, ETA)
    dd_st = np.einsum('ab,abcd,cd->', T, D0, T)
    check("van Dam-Veltman-Zakharov (1970) †: between static sources the massive (Fierz-Pauli) and massless (de Donder) "
          "numerators are 2/3 and 1/2, ratio 4/3", abs(fp_st - 2/3) < 1e-14 and abs(dd_st - 0.5) < 1e-14 and
          abs(fp_st/dd_st - 4/3) < 1e-14, f"{fp_st:.15f}, {dd_st:.15f}")

    # Legendre polynomials and the addition theorem
    x, t_ = sp.symbols('x t')
    Pl = [sp.Integer(1), x]
    for n in range(1, 8):
        Pl.append(sp.expand(((2*n + 1)*x*Pl[n] - n*Pl[n - 1])/(n + 1)))
    gen = sp.series(1/sp.sqrt(1 - 2*x*t_ + t_**2), t_, 0, 9).removeO()
    ok_b = all(sp.expand(sp.legendre(n, x) - Pl[n]) == 0 for n in range(9))
    ok_g = all(sp.expand(gen.coeff(t_, n) - Pl[n]) == 0 for n in range(9))
    ok_o = all(sp.integrate(Pl[i]*Pl[j], (x, -1, 1)) == (sp.Rational(2, 2*i + 1) if i == j else 0)
               for i in range(7) for j in range(7))
    check("Legendre P_0..P_8: sympy's legendre = Bonnet's recursion = coefficients of (1 - 2xt + t^2)^(-1/2); "
          "int P_i P_j = 2 delta_ij/(2i + 1) for i, j <= 6", ok_b and ok_g and ok_o)
    mp.mp.dps = 20
    th1, ph1, th2, ph2 = 0.7, 1.9, 2.2, -0.4
    cg = cos(th1)*cos(th2) + sin(th1)*sin(th2)*cos(ph1 - ph2)
    worst = 0.0
    for L in range(7):
        s_ = sum(mp.spherharm(L, mm, th1, ph1)*mp.conj(mp.spherharm(L, mm, th2, ph2)) for mm in range(-L, L + 1))
        worst = max(worst, float(abs(s_ - (2*L + 1)/(4*mp.pi)*mp.legendre(L, cg))))
    check("addition theorem (textbook): sum_m Y_Jm(n1) Y_Jm(n2)* = (2J+1)/(4 pi) P_J(n1.n2), J = 0..6 (mpmath): a "
          "spin-J pole's residue, the polarization sum between two vertices, is proportional to P_J of the cosine",
          worst < 1e-15, f"max deviation {worst:.1e}")

    # closed-form Legendre expansions at generic parameters (a = 0.7, alpha = 3)
    mp.mp.dps = 30
    aa, al = mp.mpf('0.7'), mp.mpf(3)
    il = lambda n, z: mp.sqrt(mp.pi/(2*z))*mp.besseli(n + mp.mpf(1)/2, z)
    dev_e = max(abs((2*n + 1)/mp.mpf(2)*mp.quad(lambda z: mp.e**(aa*z)*mp.legendre(n, z), [-1, 1]) - (2*n + 1)*il(n, aa))
                for n in range(7))
    dev_q = max(abs((2*n + 1)/mp.mpf(2)*mp.quad(lambda z: mp.legendre(n, z)/(al - z), [-1, 1]) - (2*n + 1)*mp.legenq(n, 0, al, type=3))
                for n in range(7))
    check("Legendre coefficients in closed form (generating function e^{az} = sum (2l+1) i_l(a) P_l(z); Neumann "
          "1/(alpha - z) = sum (2l+1) Q_l(alpha) P_l(z)), against quadrature at a = 0.7, alpha = 3, l = 0..6",
          dev_e < 1e-25 and dev_q < 1e-25, f"{float(dev_e):.1e}, {float(dev_q):.1e}")

    # Chebyshev min-max (textbook): brute force against the closed forms
    b_mon = minimize2(lambda c0, c1: qmax(c0, c1, 1.0, -1.0, 1.0), -2, 2, -2, 2)
    b_con = minimize2(lambda b1, b2: qmax(1.0, b1, b2, 1.0, 4.0), -2, 2, -2, 2)
    s0 = (4 + 1)/(4 - 1)
    check("Chebyshev min-max property, brute force: the monic quadratic of least sup norm on [-1, 1] has norm "
          "2^(1-n) = 1/2 (T_2/2); with P(0) = 1, min over degree-2 P of max_[1,4]|P| = 1/T_2(5/3) = 9/41",
          abs(b_mon - 0.5) < 1e-7 and b_mon >= 0.5 - 1e-12 and abs(b_con - 9/41) < 1e-7 and
          abs(1/(2*s0**2 - 1) - 9/41) < 1e-15 and b_con >= 9/41 - 1e-12, f"{b_mon:.9f}, {b_con:.9f} (9/41 = {9/41:.9f})")

    # zero-range s-wave (effective-range expansion with r_e = 0, textbook)
    k, a_ = sp.symbols('k a', positive=True)
    f = -1/(1/a_ + sp.I*k)
    sg = 4*sp.pi*sp.simplify(f*sp.conjugate(f))
    check("zero-range s-wave: f = -1/(1/a + ik) gives sigma = 4 pi a^2/(1 + k^2 a^2), obeys the optical theorem "
          "Im f = k|f|^2, and saturates the unitarity limit 4 pi/k^2 as a -> oo",
          sp.simplify(sg - 4*sp.pi*a_**2/(1 + k**2*a_**2)) == 0 and sp.simplify(sp.im(f) - k*f*sp.conjugate(f)) == 0 and
          sp.limit(k**2*sg, a_, sp.oo) == 4*sp.pi)
    print(f"      [{time.time() - T_START:.1f} s]")


# ======================================================================================================
def section_tchannel():
    print("\n== B. t-channel exchange of one massive spin-2 X, general vertex (port of "
          "derivation-gate-mechanism/gate_tchannel.py; claims C1-C7)")
    # ======================================================================================================
    # CM frame p1 = (E, k, 0, 0), p2 = (E, -k, 0, 0), p3 and p4 at angle theta; scalar chi of mass m; the most general
    # on-shell chi(p_in) -> chi(p_out) + X vertex V = F1 P P + F2 (P l + l P) + F3 l l + F4 m^2 eta, P = p_in + p_out,
    # l = p_in - p_out; the F_i are functions of t only, so constants at fixed t.
    m, M, k, q = sp.symbols('m M k q', positive=True)
    c = sp.symbols('c', real=True)
    sn = sp.sqrt(1 - c**2)
    E = sp.sqrt(m**2 + k**2)
    eta = sp.diag(1, -1, -1, -1)
    F1, F2, F3, F4 = sp.symbols('F1:5')
    S = sp.symbols('S')
    dot = lambda a, b: sp.expand((a.T*eta*b)[0, 0])
    outer = lambda a, b: a*b.T
    p1, p2 = sp.Matrix([E, k, 0, 0]), sp.Matrix([E, -k, 0, 0])
    p3, p4 = sp.Matrix([E, k*c, k*sn, 0]), sp.Matrix([E, -k*c, -k*sn, 0])
    cq = 1 - q**2/(2*k**2)                               # cos(theta) at fixed transfer q
    s_, t_, u_ = dot(p1 + p2, p1 + p2), dot(p1 - p3, p1 - p3), dot(p1 - p4, p1 - p4)
    smu = sp.expand((s_ - u_).subs(c, cq))
    check("kinematics (CM, equal masses): s = 4k^2 + 4m^2, t = -q^2, u = q^2 - 4k^2, so s - u = 8k^2 + 4m^2 - q^2 at "
          "fixed q", sp.simplify(s_ - 4*k**2 - 4*m**2) == 0 and sp.simplify(t_.subs(c, cq) + q**2) == 0 and
          sp.simplify(u_.subs(c, cq) - q**2 + 4*k**2) == 0 and sp.expand(smu - (8*k**2 + 4*m**2 - q**2)) == 0,
          f"s - u = {smu}")
    check("C1: at one vertex, p1^2 = p3^2 = m^2, p1.p3 = m^2 - t/2 and P.l = 0: the vertex's only invariant is t",
          sp.simplify(dot(p1, p1) - m**2) == 0 and sp.simplify(dot(p3, p3) - m**2) == 0 and
          sp.simplify(dot(p1, p3) - (m**2 - t_/2)) == 0 and sp.simplify(dot(p1 + p3, p1 - p3)) == 0)

    def vertex(pin, pout, f=(F1, F2, F3, F4)):
        P, l = pin + pout, pin - pout
        a, b, cc, d = f
        return a*outer(P, P) + b*(outer(P, l) + outer(l, P)) + cc*outer(l, l) + d*m**2*eta

    def G_low(l):
        ll = eta*l
        return eta - outer(ll, ll)/M**2

    def spin2(V1, V2, G):
        """V1^{mn} [ (G_mr G_ns + G_ms G_nr)/2 - G_mn G_rs/3 ] V2^{rs}  (massive spin-2 numerator)"""
        T1 = (V1.T*G*V2*G).trace()
        T2 = (V1*G*V2*G).trace()
        return sp.expand(sp.Rational(1, 2)*(T1 + T2) - sp.Rational(1, 3)*(V1*G).trace()*(V2*G).trace())

    # part 1: general vertex
    Nt = spin2(vertex(p1, p3), vertex(p2, p4), G_low(p1 - p3))
    Nt_q = sp.expand(sp.simplify(Nt.subs(c, cq)))
    Pk = sp.Poly(Nt_q, k)
    check("C2: at fixed transfer q the t-channel numerator N_t(k, q) is a polynomial in k of degree 4 (2 in k^2), "
          "lowest power k^0: no denominator in k, so no tail", Nt_q.is_polynomial(k) and Pk.degree() == 4 and
          min(mon[0] for mon in Pk.monoms()) == 0, f"degree {Pk.degree()}")
    Nt_S = sp.expand(Nt_q.subs(k, sp.sqrt((S - 4*m**2 + q**2)/8)))
    PS = sp.Poly(Nt_S, S)
    A_, B_, C_ = [sp.factor(PS.coeff_monomial(S**j)) for j in (0, 1, 2)]
    A_print = sp.sympify(
        "(-16*F1**2*M**4*m**4 - 8*F1**2*M**4*m**2*q**2 - F1**2*M**4*q**4 + 8*F1*F3*M**4*m**2*q**2 + 2*F1*F3*M**4*q**4 "
        "+ 8*F1*F3*M**2*m**2*q**4 + 2*F1*F3*M**2*q**6 - 8*F1*F4*M**4*m**4 - 2*F1*F4*M**4*m**2*q**2 - 8*F1*F4*M**2*m**4*q**2"
        " - 2*F1*F4*M**2*m**2*q**4 + 2*F3**2*M**4*q**4 + 4*F3**2*M**2*q**6 + 2*F3**2*q**8 + 2*F3*F4*M**4*m**2*q**2 "
        "- 2*F3*F4*M**2*m**2*q**4 - 4*F3*F4*m**2*q**6 - 4*F4**2*M**4*m**4 - 2*F4**2*M**2*m**4*q**2 + 2*F4**2*m**4*q**4)"
        "/(3*M**4)", locals={'F1': F1, 'F3': F3, 'F4': F4, 'M': M, 'm': m, 'q': q})
    check("C2: N_t = A(t) + B(t)(s - u) + C(t)(s - u)^2 with C = F1^2, B = 2 F2^2 q^2 (M^2 + q^2)/M^2, and A the "
          "printed degree-8 polynomial in q over 3M^4", PS.degree() == 2 and sp.simplify(C_ - F1**2) == 0 and
          sp.simplify(B_ - 2*F2**2*q**2*(M**2 + q**2)/M**2) == 0 and sp.simplify(A_ - A_print) == 0,
          f"C = {C_}, B = {B_}")

    Res = sp.expand(Nt_q.subs(q, sp.I*M))                  # residue numerator at the pole t = M^2
    dres = [sp.simplify(sp.diff(Res, F)) for F in (F2, F3, F4)]
    z = sp.symbols('z')
    P2 = (3*z**2 - 1)/2
    Ssub = sp.expand((s_ - u_).subs(c, cq).subs(q, sp.I*M))
    target = sp.Rational(2, 3)*F1**2*(4*m**2 - M**2)**2*P2.subs(z, Ssub/(4*m**2 - M**2))
    check("C3: the residue at t = M_X^2 does not depend on F2, F3, F4", dres == [0, 0, 0], f"{dres}")
    check("C3: residue = (2/3) F1^2 (4m^2 - M_X^2)^2 P_2(z_t), z_t = (s - u)/(4m^2 - M_X^2)",
          sp.simplify(Res - target) == 0)
    rem = {}
    for label, fsub in (("const", {}),
                        ("linear", {F: sp.Symbol('a%d' % i) + sp.Symbol('b%d' % i)*(-q**2)
                                    for i, F in enumerate((F1, F2, F3, F4), start=1)})):
        Nf = sp.expand(Nt_q.subs(fsub, simultaneous=True))
        Rf = sp.expand(Nf.subs(q, sp.I*M))
        num, den = sp.fraction(sp.together(sp.cancel((Nf - Rf)/(-q**2 - M**2))))
        rem[label] = (sp.factor(den), sp.expand(num).is_polynomial(k, q), sp.Poly(num, k).degree())
    check("C3: the non-pole remainder is a polynomial in (k, q) over 3 M_X^4: degree 2 in k for constant F_i, "
          "degree 4 for F_i = a_i + b_i t (a contact term, quadratic in s)",
          rem['const'] == (3*M**4, True, 2) and rem['linear'] == (3*M**4, True, 4), f"{rem}")

    # part 2: minimal coupling X_mn T^mn
    fmin = (sp.Rational(1, 2), 0, -sp.Rational(1, 2), t_/(2*m**2))
    Vmin = vertex(p1, p3, fmin)
    cons = sp.simplify((eta*(p1 - p3)).T*Vmin)
    check("C4: the minimal vertex <p_out|T^{mu nu}|p_in> = 1/2 P P - 1/2 l l + (t/2) eta is conserved: "
          "l_mu V^{mu nu} = 0", all(x_ == 0 for x_ in cons))
    Nmin = spin2(Vmin, vertex(p2, p4, fmin), G_low(p1 - p3))
    formula = (s_ - u_)**2/4 + t_**2/4 + 2*m**2*t_ - sp.Rational(1, 3)*(2*m**2 + t_)**2
    check("C4: minimal-coupling numerator N_min = (s - u)^2/4 + t^2/4 + 2m^2 t - (2m^2 + t)^2/3",
          sp.simplify(Nmin - formula) == 0)
    Nmin_q = sp.expand(sp.simplify(Nmin.subs(c, cq)))
    N00 = sp.simplify(Nmin_q.subs({k: 0, q: 0}))
    fwd = sp.expand(sp.simplify(Nmin_q.subs(q, 0)/N00))
    kdep = sp.expand(sp.simplify(Nmin_q.subs(k, 0)/N00))
    check("C4: N_min(0, 0) = 8m^4/3, and the forward ratio N_min(k, 0)/N_min(0, 0) = 1 + 6k^2/m^2 + 6k^4/m^4: "
          "its k-scale is m/sqrt6, a relative speed of order c",
          sp.simplify(N00 - 8*m**4/3) == 0 and sp.expand(fwd - (1 + 6*k**2/m**2 + 6*k**4/m**4)) == 0, f"{fwd}")
    check("C4: at k = 0 the transfer dependence is N_min(0, q)/N_min(0, 0) = 1 - q^2/m^2 + q^4/(16 m^4)",
          sp.expand(kdep - (1 - q**2/m**2 + q**4/(16*m**4))) == 0, f"{kdep}")

    # part 3: generic vertex at q = 0
    P0 = sp.Poly(sp.expand(Nt_q.subs(q, 0)), k)
    n0, n1, n2 = [sp.factor(P0.coeff_monomial(k**j)) for j in (0, 2, 4)]
    check("C5: at q = 0, N_t = n0 + n1 k^2 + n2 k^4 with n1 = 64 F1^2 m^2 >= 0, n2 = 64 F1^2 >= 0 and "
          "n0 = 4m^4 (2F1 - F4)(4F1 + F4)/3: the forward numerator never decreases with k^2 except toward one zero",
          P0.degree() == 4 and sp.simplify(n1 - 64*F1**2*m**2) == 0 and sp.simplify(n2 - 64*F1**2) == 0 and
          sp.simplify(n0 - 4*m**4*(2*F1 - F4)*(4*F1 + F4)/3) == 0 and
          sp.Poly(sp.expand(Nt_q.subs(q, 0)), k).coeff_monomial(k**1) == 0 and P0.coeff_monomial(k**3) == 0,
          f"n0 = {n0}, n1 = {n1}, n2 = {n2}")
    ksc = sp.factor(n0/n1)
    kmin = sp.simplify(ksc.subs({F1: sp.Rational(1, 2), F4: 0}))
    check("C5: k-scale^2 = n0/n1 = m^2 (2F1 - F4)(4F1 + F4)/(48 F1^2); for minimal coupling (F1 = 1/2, F4 = t/2m^2 = 0 "
          "at q = 0) it is m^2/6", sp.simplify(ksc - m**2*(2*F1 - F4)*(4*F1 + F4)/(48*F1**2)) == 0 and
          kmin == m**2/6, f"{ksc}; minimal {kmin}")

    # part 4: u-channel (identical chi), forward
    Nu = spin2(vertex(p1, p4, fmin), vertex(p2, p3, fmin), G_low(p1 - p4))
    Nu_q0 = sp.simplify(Nu.subs(c, 1))
    den_u = sp.simplify(u_.subs(c, 1) - M**2)
    ser = sp.series(sp.simplify(Nu_q0/den_u), k, 0, 5).removeO()
    ser_print = (-8*m**4/(3*M**2) + k**2*(-8*m**2/(3*M**2) + 32*m**4/(3*M**4)) +
                 k**4*(-8/(3*M**2) + 64*m**2/(3*M**4) - 128*m**4/(3*M**6)))
    check("C6: forward u-channel (identical chi, minimal coupling): u - M_X^2 = -(M_X^2 + 4k^2), so the term is "
          "rational in k with scale M_X/2; its series -8m^4/(3M^2) + k^2(-8m^2/(3M^2) + 32m^4/(3M^4)) + ... reproduces",
          sp.simplify(den_u + M**2 + 4*k**2) == 0 and Nu_q0.is_polynomial(k) and sp.expand(ser - ser_print) == 0)
    g = sp.symbols('g', positive=True)
    Afwd = g**2*(1/(0 - M**2) + 1/den_u)
    rat = sp.simplify(Afwd/Afwd.subs(k, 0))
    lim = sp.limit(rat, k, sp.oo)
    check("C6: spin-0 forward t + u: A(k)/A(0) = (M^2 + 2k^2)/(M^2 + 4k^2) -> 1/2: the u-channel halves the forward "
          "amplitude, it does not gate it", sp.simplify(rat - (M**2 + 2*k**2)/(M**2 + 4*k**2)) == 0 and
          lim == sp.Rational(1, 2), f"{rat}, limit {lim}")

    # part 5: s-channel (chi chibar only)
    G1, G2, G3, G4 = sp.symbols('G1:5')
    def vertex_s(pa, pb, f=(G1, G2, G3, G4)):
        P, r = pa + pb, pa - pb
        a, b, cc, d = f
        return a*outer(r, r) + b*outer(P, P) + cc*(outer(P, r) + outer(r, P)) + d*m**2*eta
    Ns = spin2(vertex_s(p1, p2), vertex_s(p3, p4), G_low(p1 + p2))
    Rs = sp.simplify(Ns.subs(M, sp.sqrt(s_)))
    delta = sp.symbols('delta', positive=True)
    pole = Rs/(s_ - 4*(m**2 - delta))
    check("C6: s-channel (chi chibar) residue at s = M_X^2 is (32/3) G1^2 k^4 P_2(cos theta) = 16 G1^2 k^4 (3c^2 - 1)/3: "
          "d-wave, independent of G2-G4", sp.simplify(Rs - sp.Rational(32, 3)*G1**2*k**4*P2.subs(z, c)) == 0,
          f"{sp.factor(Rs)}")
    check("C6: with the pole just below threshold (M_X^2 = 4(m^2 - delta)) the s-channel term "
          "G1^2 k^4 (4c^2 - 4/3)/(delta + k^2) -> 0 as k -> 0: it vanishes at threshold (an anti-gate)",
          sp.simplify(pole - G1**2*k**4*(4*c**2 - sp.Rational(4, 3))/(delta + k**2)) == 0 and sp.limit(pole, k, 0) == 0)

    # part 6: Legendre coefficients of a non-polynomial residue
    zz = sp.symbols('zz', real=True)
    ce = [float(sp.N((2*l + 1)/sp.Integer(2)*sp.integrate(sp.exp(-zz)*sp.legendre(l, zz), (zz, -1, 1)), 15)) for l in range(7)]
    cr = [float(sp.N((2*l + 1)/sp.Integer(2)*sp.integrate(sp.legendre(l, zz)/(2 - zz), (zz, -1, 1)), 15)) for l in range(7)]
    pe = [1.17520, -1.10364, 0.357814, -0.0704556, 0.00996513, -0.00109959, 9.94543e-5]
    pr = [0.549306, 0.295837, 0.105919, 0.0340978, 0.0104497, 0.00311274, 0.000910235]
    mp.mp.dps = 30
    cfe = [float((2*l + 1)*(-1)**l*mp.sqrt(mp.pi/2)*mp.besseli(l + mp.mpf(1)/2, 1)) for l in range(7)]
    qls = [mp.legenq(l, 0, mp.mpf(2), type=3) for l in range(7)]   # mpc with zero imaginary part off the cut
    assert all(mp.im(x_) == 0 for x_ in qls)
    cfr = [float((2*l + 1)*mp.re(x_)) for l, x_ in enumerate(qls)]
    check("C7: Legendre coefficients of exp(-z), l = 0-6: 1.17520, -1.10364, 0.357814, -0.0704556, 0.00996513, "
          "-0.00109959, 9.94543e-5, all nonzero, = (2l+1) i_l(-1)",
          all(sig(x_, 6) == y_ for x_, y_ in zip(ce, pe)) and all(abs(x_ - y_) < 1e-14 for x_, y_ in zip(ce, cfe)) and
          all(x_ != 0 for x_ in ce), ", ".join(f"{x_:.6g}" for x_ in ce))
    check("C7: Legendre coefficients of 1/(2 - z), l = 0-6: 0.549306, 0.295837, 0.105919, 0.0340978, 0.0104497, "
          "0.00311274, 0.000910235, all nonzero, = (2l+1) Q_l(2): a non-polynomial residue F(s) needs every spin",
          all(sig(x_, 6) == y_ for x_, y_ in zip(cr, pr)) and all(abs(x_ - y_) < 1e-14 for x_, y_ in zip(cr, cfr)) and
          all(x_ != 0 for x_ in cr), ", ".join(f"{x_:.6g}" for x_ in cr))
    print(f"      [{time.time() - T_START:.1f} s]")
    return dict(N00=N00, fwd=fwd, n1=n1, n2=n2, m=m, k=k, vertex=vertex, fmin=fmin, p=(p1, p2, p3, p4), c=c,
                eta=eta, Ssub=Ssub, M=M, s=s_, u=u_, t=t_)


# ======================================================================================================
def section_fermion():
    print("\n== C. Dirac chi (port of derivation-gate-mechanism/gate_fermion.py; claim C4)")
    # ======================================================================================================
    # V^{mn} = (1/4) ubar_out [g^m P^n + g^n P^m] u_in + kappa/(4m) ubar_out [i sigma^{m a} l_a P^n + (m <-> n)] u_in;
    # m = 1, M_X = 0.5, Dirac representation. The ratio printed is (|A(k)|/|A(k0)| - 1)/((k^2 - k0^2)/m^2).
    m, M = 1.0, 0.5
    I2, Z2 = np.eye(2), np.zeros((2, 2))
    sig_ = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    gam = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in sig_]
    def spinor(p, xi):
        E = p[0]
        sp_ = sum(p[i + 1]*sig_[i] for i in range(3))
        return np.concatenate([np.sqrt(E + m)*xi, (sp_ @ xi)/np.sqrt(E + m)])
    bar = lambda u: u.conj() @ gam[0]
    def vertex(pin, pout, uin, uout, kappa):
        P, l = pin + pout, pin - pout
        l_low = ETA @ l
        V = np.zeros((4, 4), complex)
        for a in range(4):
            for b in range(4):
                V[a, b] = 0.25*bar(uout) @ (gam[a]*P[b] + gam[b]*P[a]) @ uin
                if kappa:
                    for (x, y) in ((a, b), (b, a)):
                        sxl = sum(0.5j*(gam[x] @ gam[al] - gam[al] @ gam[x])*l_low[al] for al in range(4))
                        V[a, b] += kappa/(4*m)*bar(uout) @ (1j*sxl*P[y]) @ uin
        return V
    def spin2(V1, V2, l):
        ll = ETA @ l
        G = ETA - np.outer(ll, ll)/M**2
        return 0.5*(np.trace(V1.T @ G @ V2 @ G) + np.trace(V1 @ G @ V2 @ G)) - np.trace(V1 @ G)*np.trace(V2 @ G)/3.0
    def amp(k, q, kappa, spins):
        c = 1 - q**2/(2*k**2)
        s = np.sqrt(max(0.0, 1 - c**2))
        E = np.sqrt(m**2 + k**2)
        p1, p2 = np.array([E, k, 0, 0]), np.array([E, -k, 0, 0])
        p3, p4 = np.array([E, k*c, k*s, 0]), np.array([E, -k*c, -k*s, 0])
        xi = {'u': np.array([1, 0], complex), 'd': np.array([0, 1], complex)}
        s1, s2, s3, s4 = (xi[ch] for ch in spins)
        return spin2(vertex(p1, p3, spinor(p1, s1), spinor(p3, s3), kappa),
                     vertex(p2, p4, spinor(p2, s2), spinor(p4, s4), kappa), p1 - p3)
    # the printed table: (q, kappa, spins) -> (|A(k0)| to 6 figures, ratios to 4 decimals)
    printed = {
        (2e-3, 0.0, 'uuuu'): ("2.66667", "6.0000 6.0006 6.0054 6.0600"),
        (2e-3, 0.0, 'udud'): ("2.66668", "6.0000 6.0006 6.0054 6.0600"),
        (2e-3, 0.0, 'uudd'): ("2e-06", "2.0000 2.0000 2.0000 2.0000"),
        (2e-3, 0.7, 'uuuu'): ("2.66668", "6.0000 6.0006 6.0054 6.0600"),
        (2e-3, 0.7, 'udud'): ("2.66668", "6.0000 6.0006 6.0054 6.0600"),
        (2e-3, 0.7, 'uudd'): ("3.20001e-07", "2.0000 2.0000 2.0000 2.0000"),
        (0.1, 0.0, 'uuuu'): ("2.68603", "6.0372 6.2141 6.5097"),
        (0.1, 0.0, 'udud'): ("2.69601", "6.0006 6.1786 6.4753"),
        (0.1, 0.0, 'uudd'): ("0.0050235", "1.9906 1.9906 1.9906"),
        (0.1, 0.7, 'uuuu'): ("2.70903", "6.0033 6.1810 6.4774"),
        (0.1, 0.7, 'udud'): ("2.71063", "5.9974 6.1754 6.4720"),
        (0.1, 0.7, 'uudd'): ("0.00080376", "1.9906 1.9906 1.9906")}
    kgrid = {2e-3: [1.2e-3, 3e-3, 1e-2, 3e-2, 1e-1], 0.1: [0.06, 0.1, 0.2, 0.3]}
    got, bad, rel01 = {}, [], None
    for (q, kappa, spins), (a0s, rs) in printed.items():
        ks = kgrid[q]
        A0 = amp(ks[0], q, kappa, spins)
        rels = [abs(amp(kk, q, kappa, spins))/abs(A0) - 1 for kk in ks[1:]]
        ratios = [r_/((kk**2 - ks[0]**2)/m**2) for r_, kk in zip(rels, ks[1:])]
        got[(q, kappa, spins)] = ratios
        if q == 2e-3 and kappa == 0.0 and spins == 'uuuu':
            rel01 = rels[1]
        if f"{abs(A0):.6g}" != a0s or " ".join(f"{r_:.4f}" for r_ in ratios) != rs:
            bad.append((q, kappa, spins, f"{abs(A0):.6g}", " ".join(f"{r_:.4f}" for r_ in ratios)))
    check("C4: Dirac chi, with and without a magnetic-type structure (kappa = 0, 0.7): all 12 printed rows of "
          "|A(k0)| and (|A(k)|/|A(k0)| - 1)/((k^2 - k0^2)/m^2) reproduce (q/m = 2e-3 and 0.1)", not bad, f"{bad}")
    # scalar chi at the same (k, k0, q): N_min = (s - u)^2/4 + t^2/4 + 2m^2 t - (2m^2 + t)^2/3 (section B)
    Nsc = lambda k, q: (8*k*k + 4*m*m - q*q)**2/4 + q**4/4 - 2*m*m*q*q - (2*m*m - q*q)**2/3
    def scal(q):
        ks = kgrid[q]
        return [(Nsc(kk, q)/Nsc(ks[0], q) - 1)/((kk**2 - ks[0]**2)/m**2) for kk in ks[1:]]
    pres = {key: v for key, v in got.items() if key[0] == 2e-3 and key[2] != 'uudd'}
    flip = [r_ for key, v in got.items() if key[0] == 2e-3 and key[2] == 'uudd' for r_ in v]
    sc2, sc1 = scal(2e-3), scal(0.1)
    check("C4: Dirac chi gives the same coefficient as scalar chi, 6.00 (6.0006 at k/m = 0.01, q/m = 2e-3, where "
          "|A(k)|/|A(k0)| - 1 = 5.9142e-4): at q/m = 2e-3 all four spin-preserving rows (uuuu, udud; kappa = 0, 0.7) equal "
          "scalar chi's N_min ratio at the same (k, k0, q), 6.0000, 6.0006, 6.0054, 6.0600, to 4 decimals",
          f"{got[(2e-3, 0.0, 'uuuu')][1]:.4f}" == "6.0006" and f"{rel01:.4e}" == "5.9142e-04" and
          all([f"{r_:.4f}" for r_ in v] == [f"{r_:.4f}" for r_ in sc2] for v in pres.values()),
          f"scalar {', '.join(f'{r_:.4f}' for r_ in sc2)}; at q/m = 0.1 scalar {', '.join(f'{r_:.4f}' for r_ in sc1)}, "
          f"Dirac 6.00-6.04, 6.18-6.21, 6.47-6.51")
    check("C4, spin-flip channel (printed in gate_fermion.out, not in C4's text): the uudd amplitude, 1e-6 of the others "
          "at q/m = 2e-3, has coefficient 2.0000 (1.9906 at q/m = 0.1), also of order one: the k-scale is m in every "
          "helicity channel", all(f"{r_:.4f}" == "2.0000" for r_ in flip), f"{min(flip):.6f}-{max(flip):.6f}")


# ======================================================================================================
def section_numbers():
    print("\n== D. Numbers in run 4's convention, mu c = 20 keV (port of derivation-gate-mechanism/gate_numbers.py; "
          "claims C4, C5, C6, C8, C9, C14, C19)")
    # ======================================================================================================
    m, mu = M_CHI, MU_R4
    vstar, va = VSTAR_R4, VA_R4
    check("C19: mu/m = 2.8571e-4; v* = sqrt2 (mu/m) c = 121.1 km/s; v_a = sqrt2 v* = 2 (mu/m) c = 171.3 km/s",
          sig(mu/m, 5) == 2.8571e-4 and round(vstar, 1) == 121.1 and round(va, 1) == 171.3,
          f"{mu/m:.4e}, {vstar:.4f}, {va:.4f} km/s")
    check("C9/C11: hbar/(mu c) = 9866 fm = 9.87 pm (the range of the R1 potential, the nonlocality of R2)",
          round(HBARC/mu) == 9866 and round(HBARC/mu/1e3, 2) == 9.87, f"{HBARC/mu:.2f} fm")
    check("C6: hbar/(M_X c) at M_X = 2 mu = 40 keV is 4.93 pm", round(HBARC/(2*mu)/1e3, 2) == 4.93,
          f"{HBARC/(2*mu)/1e3:.4f} pm")
    check("C5: (m/mu)^2 = 1.225e7: a k-scale mu in the degree-2 numerator needs n0 cancelled to (mu/m)^2 = 1/(1.2e7)",
          sig((m/mu)**2, 4) == 1.225e7, f"{(m/mu)**2:.6e}")

    # t-channel (minimal coupling) against the record's gate, forward amplitude
    rows = {50: ("8.3391e-05", "4.1724e-08", "9.1834e-01", "8.4335e-01"),
            120: ("2.0014e-04", "2.4033e-07", "6.1221e-01", "3.7480e-01"),
            171.3: ("2.8570e-04", "4.8974e-07", "3.6792e-01", "1.3537e-01"),
            300: ("5.0035e-04", "1.5021e-06", "4.6573e-02", "2.1690e-03"),
            1500: ("2.5017e-03", "3.7552e-05", "5.0498e-34", "2.5501e-67")}
    bad = []
    for v, want in rows.items():
        km = v/(2*C_KMS)
        got = tuple(f"{x_:.4e}" for x_ in (km, 6*km**2 + 6*km**4, exp(-(m*km/mu)**2), exp(-v**2/vstar**2)))
        print(f"      v = {v:6} km/s: k/m = {got[0]}, X: N(k)/N(0) - 1 = {got[1]}, gate exp(-k^2/mu^2) = {got[2]}, "
              f"sigma gate = {got[3]}")
        if got != want:
            bad.append((v, got))
    check("C4: the table of k/m, X's forward k-dependence 6k^2/m^2 + 6k^4/m^4, the amplitude gate exp(-k^2/mu^2) and "
          "the cross-section gate exp(-v^2/v*^2) at v = 50, 120, 171.3, 300, 1500 km/s reproduces (k = m v/2)",
          not bad, f"{bad}")
    k120, k1500 = 120/(2*C_KMS), 1500/(2*C_KMS)
    check("C4: X's k-dependence is 2.4e-7 at 120 km/s and 3.8e-5 at 1500 km/s, where the gate exp(-k^2/mu^2) falls "
          "from 0.61 to 5e-34", sig(6*k120**2 + 6*k120**4, 2) == 2.4e-7 and sig(6*k1500**2 + 6*k1500**4, 2) == 3.8e-5
          and sig(exp(-(m*k120/mu)**2), 2) == 0.61 and sig(exp(-(m*k1500/mu)**2), 1) == 5e-34)
    v_O1 = 2*C_KMS/sqrt(6)
    # the same condition read relativistically (my addition, flagged in the report): 6k^2/m^2 = 1 at gamma = 4/3
    v_rel_rel = sqrt(1 - (3/4)**2)
    check("C4: X's k-dependence reaches order one (6k^2/m^2 = 1) at v_rel = 2c/sqrt6 = 244780 km/s = 0.816c, "
          "1429 times v_a (with k = m v/2)", f"{v_O1:.0f}" == "244780" and round(v_O1/C_KMS, 3) == 0.816 and
          round(v_O1/va) == 1429, f"{v_O1:.2f} km/s; read relativistically (gamma = 1 + 2k^2/m^2 = 4/3) the relative "
          f"speed is {v_rel_rel:.3f}c")

    # no degree-2 polynomial in x = k^2/mu^2 with P(0) = 1 can gate
    a_, b_ = 1.0, (1500/va)**2
    s0 = (b_ + a_)/(b_ - a_)
    T2 = lambda y: 2*y**2 - 1
    bound = 1/T2(s0)
    xs = np.linspace(a_, b_, 200001)
    Pstar = T2((2*xs - (a_ + b_))/(b_ - a_))/T2((0 - (a_ + b_))/(b_ - a_))
    alt = [T2((2*x_ - (a_ + b_))/(b_ - a_))/T2(s0) for x_ in (a_, (a_ + b_)/2, b_)]
    check("C5: on x in [1, 76.7] (v_a to 1500 km/s) the Chebyshev bound is 1/T_2(1.02643) = 0.90324; P* attains it "
          "(max|P*| = 0.90324 on a 200001-point grid, P*(0) = 1) and equioscillates (+, -, + at x = 1, mid, 76.7), so "
          "by de la Vallee Poussin no degree-2 P with P(0) = 1 stays below 0.903 in magnitude",
          round(b_, 1) == 76.7 and round(s0, 5) == 1.02643 and round(bound, 5) == 0.90324 and
          round(np.abs(Pstar).max(), 5) == 0.90324 and abs(alt[0] - bound) < 1e-15 and abs(alt[1] + bound) < 1e-15 and
          abs(alt[2] - bound) < 1e-15, f"{bound:.8f}; alternation {[round(x_, 6) for x_ in alt]}")
    best_bf = minimize2(lambda b1, b2: qmax(1.0, b1, b2, a_, b_), -1, 1, -0.05, 0.05)
    # the record's random search (seed 0): b1 ~ U(-0.2, 0.05), b2 ~ U(-0.002, 0.004), interleaved; max|P| on 4001 points
    r = np.random.default_rng(0).random(400000)
    b1s, b2s = -0.2 + 0.25*r[0::2], -0.002 + 0.006*r[1::2]
    xg = np.linspace(a_, b_, 4001)
    h = xg[1] - xg[0]
    with np.errstate(divide='ignore', invalid='ignore'):
        xv = np.where(b2s != 0, -b1s/(2*b2s), a_)
    j = np.clip(np.floor((xv - a_)/h).astype(np.int64), 0, len(xg) - 2)      # the grid points around the vertex
    Pv = lambda x_: np.abs(1 + b1s*x_ + b2s*x_**2)
    gmax = np.maximum(np.maximum(Pv(xg[0]), Pv(xg[-1])), np.maximum(Pv(xg[j]), Pv(xg[j + 1])))
    full = np.abs(1 + b1s[:500, None]*xg[None, :] + b2s[:500, None]*xg[None, :]**2).max(axis=1)
    check("C5: brute force agrees: convex minimization gives 0.90324; the record's random search (2e5 trials, seed 0) "
          "best max|P| = 0.90378, never below the bound",
          round(best_bf, 5) == 0.90324 and best_bf >= bound - 1e-12 and round(gmax.min(), 5) == 0.90378 and
          gmax.min() >= bound and np.abs(full - gmax[:500]).max() < 1e-12, f"{best_bf:.8f}, {gmax.min():.8f}")
    check("C5: over the same range the Gaussian amplitude gate falls from 3.679e-1 to 5.050e-34",
          f"{exp(-1.0):.3e}" == "3.679e-01" and f"{exp(-b_):.3e}" == "5.050e-34")

    sig0 = 16*pi*(HBARC/m)**2*1e-26                      # fm^2 -> cm^2
    s0m = sig0/(m*MEV_G)
    check("C19: contact Born benchmark sigma0 = 16 pi alpha~^2 m^2/m_phi^4 (alpha~ = 1, m_phi = m) = 3.9944e-24 cm^2: "
          "sigma0/m = 32.01 cm^2/g at 70 MeV, m = 71.5 MeV for 30 cm^2/g",
          sig(sig0, 5) == 3.9944e-24 and round(s0m, 2) == 32.01 and round(m*(s0m/30)**(1/3), 1) == 71.5,
          f"{sig0:.6e} cm^2, {s0m:.4f} cm^2/g, {m*(s0m/30)**(1/3):.3f} MeV")
    sres = 4*pi*(HBARC/mu)**2*1e-26
    check("C8: a zero-energy state with 1/a = mu gives sigma(k -> 0) = 4 pi a^2 = 1.2233e-17 cm^2, sigma/m = "
          "9.803e7 cm^2/g at 70 MeV, 3.27e6 times 30 cm^2/g",
          sig(sres, 5) == 1.2233e-17 and sig(sres/(m*MEV_G), 4) == 9.803e7 and sig(sres/(m*MEV_G)/30, 3) == 3.27e6,
          f"{sres:.5e} cm^2, {sres/(m*MEV_G):.5e} cm^2/g")
    supp = [exp(-2*V**2/vstar**2) for V in (100, 300, 600)]
    check("C14: a preferred-frame vertex suppresses a pair moving at V by exp(-m^2 V^2/mu^2) = exp(-2V^2/v*^2): "
          "2.559e-1, 4.705e-6, 4.899e-22 at V = 100, 300, 600 km/s",
          [f"{x_:.3e}" for x_ in supp] == ["2.559e-01", "4.705e-06", "4.899e-22"], ", ".join(f"{x_:.4e}" for x_ in supp))
    print(f"      [{time.time() - T_START:.1f} s]")


# ======================================================================================================
def section_fiber():
    print("\n== E. #6 s4's fiber overlap in field-theory terms (port of derivation-gate-mechanism/fiber_overlap.py; "
          "claims C1, C9-C11)")
    # ======================================================================================================
    # Wigner density W(x,p) = int dy e^{ipy} psi*(x + y/2) psi(x - y/2). R1 (one-body overlap):
    # H = int dx dp dp' W(x,p) S(p - p') W(x,p'). R2 (pair channel): H = B+ B, B(x) = int dy gt(y) psi(x+y/2) psi(x-y/2).
    k1 = sp.Matrix(sp.symbols('k1x k1y k1z')); k2 = sp.Matrix(sp.symbols('k2x k2y k2z'))
    k3 = sp.Matrix(sp.symbols('k3x k3y k3z')); k4 = k1 + k2 - k3
    d13 = sp.simplify((k1 + k3)/2 - (k2 + k4)/2)
    d14 = sp.simplify((k1 + k4)/2 - (k2 + k3)/2)
    check("C1/C9: a bilinear's fiber coordinate is the average momentum; with k1 + k2 = k3 + k4 the fiber separation of "
          "the two bilinears is k1 - k4 (pairing 1->3, 2->4) or k1 - k3 (pairing 1->4, 2->3): a momentum transfer",
          sp.simplify(d13 - (k1 - k4)) == sp.zeros(3, 1) and sp.simplify(d14 - (k1 - k3)) == sp.zeros(3, 1))
    k, q, mu = sp.symbols('k q mu', positive=True)
    K1, K2 = sp.Matrix([k, 0, 0]), sp.Matrix([-k, 0, 0])
    th = sp.acos(1 - q**2/(2*k**2))
    K3 = sp.Matrix([k*sp.cos(th), k*sp.sin(th), 0]); K4 = -K3
    d2 = [sp.simplify((K1 - K3).dot(K1 - K3)), sp.simplify((K1 - K4).dot(K1 - K4)), sp.simplify((K1 - K2).dot(K1 - K2))]
    check("C9: in the CM frame |k1 - k3|^2 = q^2, |k1 - k4|^2 = 4k^2 - q^2 (= q_u^2), |k1 - k2|^2 = 4k^2",
          d2[0] == q**2 and sp.expand(d2[1] - 4*k**2 + q**2) == 0 and d2[2] == 4*k**2, f"{d2}")
    S = lambda dd: sp.exp(-dd/(2*mu**2))
    amp = S(d2[0]) + S(d2[1])
    a0 = sp.simplify(sp.limit(amp, q, 0))
    ainf = sp.limit(a0, k, sp.oo)
    check("C9: R1's Born amplitude for identical chi is S(q) + S(q_u); at q -> 0 it is 1 + exp(-2k^2/mu^2) (#6's "
          "exp(-(p1 - p2)^2/2mu^2) is only the exchange term's forward value) and it tends to 1, not 0, at large k",
          sp.simplify(a0 - 1 - sp.exp(-2*k**2/mu**2)) == 0 and ainf == 1, f"{a0}; k -> oo: {ainf}")
    y, P, D = sp.symbols('y P Delta', real=True)
    p_, pp_ = P + D/2, P - D/2
    jac = sp.Matrix([[sp.diff(p_, P), sp.diff(p_, D)], [sp.diff(pp_, P), sp.diff(pp_, D)]]).det()
    St = sp.simplify(sp.integrate(sp.exp(sp.I*D*y)*sp.exp(-D**2/(2*mu**2)), (D, -sp.oo, sp.oo)))
    check("C9: as an operator R1 is x-local: (p, p') -> (P, Delta) has |Jacobian| = 1, the P integral gives "
          "2 pi delta(y + y'), and St(y) = int dDelta e^{i Delta y} S(Delta) = sqrt(2 pi) mu exp(-mu^2 y^2/2), so "
          "V(r) = 2 pi St(r), a Gaussian of width 1/mu in position", abs(jac) == 1 and
          sp.simplify(St - sp.sqrt(2*sp.pi)*mu*sp.exp(-mu**2*y**2/2)) == 0, f"St = {St}")

    def packet(x, x0, p0, sx):
        return (2*np.pi*sx**2)**-0.25*np.exp(-(x - x0)**2/(4*sx**2) + 1j*p0*x)
    def wigner(phi, x, y, pgrid):
        X, Y = np.meshgrid(x, y, indexing='ij')
        integrand = np.conj(phi(X + Y/2))*phi(X - Y/2)
        return integrand @ np.exp(1j*np.outer(y, pgrid))*(y[1] - y[0])
    x = np.linspace(-9, 9, 361); dx = x[1] - x[0]
    yg = np.linspace(-18, 18, 721)
    pg = np.linspace(-7, 7, 281); dp = pg[1] - pg[0]
    sx = 1.0
    res = []
    for (x1, p1, x2, p2, mu_) in ((0.0, 0.3, 0.7, -0.5, 0.8), (0.4, 1.0, -0.3, -0.2, 1.7)):
        ph1 = lambda z: packet(z, x1, p1, sx)
        ph2 = lambda z: packet(z, x2, p2, sx)
        W1, W2 = wigner(ph1, x, yg, pg), wigner(ph2, x, yg, pg)
        Smat = np.exp(-(pg[:, None] - pg[None, :])**2/(2*mu_**2))
        I_phase = np.einsum('xp,pq,xq->', W1, Smat, W2)*dx*dp*dp
        A, B = np.meshgrid(x, x, indexing='ij')
        St_num = np.sqrt(2*np.pi)*mu_*np.exp(-mu_**2*(A - B)**2/2)
        I_pos = 2*np.pi*(np.conj(ph1(x))*ph2(x) @ St_num @ (np.conj(ph2(x))*ph1(x)))*dx*dx
        res.append((I_phase, I_pos))
    check("C9: 1D quadrature for two wavepacket pairs: the phase-space overlap equals 2 pi times the exchange integral "
          "of V: 5.57550319 = 5.57550319 and 7.35636496 = 7.35636496 (imaginary parts < 1e-15)",
          [f"{r_[0].real:.8f}" for r_ in res] == ["5.57550319", "7.35636496"] and
          [f"{r_[1].real:.8f}" for r_ in res] == ["5.57550319", "7.35636496"] and
          max(abs(r_[i].imag) for r_ in res for i in (0, 1)) < 1e-15,
          "; ".join(f"{r_[0].real:.10f} vs {r_[1].real:.10f}" for r_ in res))
    ovs, want = [], {(0.0, 1.0): "0.367879", (1.0, 0.0): "0.778801", (2.0, 0.0): "0.367879", (0.0, 2.0): "0.018316"}
    for (dxs, dps), w in want.items():
        ov = abs(np.sum(np.conj(packet(x, 0.0, 0.0, sx))*packet(x, dxs, dps, sx))*dx)**2
        form = np.exp(-dps**2/(4*(1/(2*sx))**2) - dxs**2/(4*sx**2))
        ovs.append((f"{ov:.6f}", f"{form:.6f}", w))
    check("C9: the packet overlap (the mu -> 0 limit) is a state property: |<1|2>|^2 = 0.367879 at dp = 1 and at "
          "dx = 2 (sigma_x = 1), 0.778801 at dx = 1, 0.018316 at dp = 2, = exp(-dp^2/(4 sp^2) - dx^2/(4 sx^2))",
          all(a_ == b_ == c_ for a_, b_, c_ in ovs), f"{[o_[0] for o_ in ovs]}")
    xs_, ys_ = sp.symbols('x y', real=True)
    ka, kb = sp.symbols('k_a k_b', real=True)
    phase = sp.expand(sp.I*ka*(xs_ + ys_/2) + sp.I*kb*(xs_ - ys_/2))
    check("C11: R2's pair bilinear psi(x + y/2) psi(x - y/2) on plane waves has phase i(k_a + k_b) x + i(k_a - k_b) y/2: "
          "the vertex sees the pair's relative momentum (k_a - k_b)/2, and the separable amplitude g(k) g*(k') = "
          "|g(k)|^2 on shell is the gate", sp.expand(phase.coeff(ys_) - sp.I*(ka - kb)/2) == 0 and
          sp.expand(phase.coeff(xs_) - sp.I*(ka + kb)) == 0)

    # transfer cross-sections (Born, unit couplings; shapes only)
    cc = sp.symbols('cc', real=True)
    SG = lambda q2: sp.exp(-q2/(2*mu**2))
    qt2, qu2 = 2*k**2*(1 - cc), 2*k**2*(1 + cc)
    sig_R2 = sp.exp(-2*k**2/mu**2)
    sig_R1_id = 2*sp.pi*sp.integrate(sp.expand((1 - cc**2)*(SG(qt2) + SG(qu2))**2), (cc, -1, 1))
    sig_R1_maj = 2*sp.pi*sp.integrate((1 - cc)*SG(qu2)**2, (cc, -1, 1))
    Mx = sp.symbols('M_X', positive=True)
    sig_yuk = 2*sp.pi*sp.integrate((1 - cc)/(qt2 + Mx**2)**2, (cc, -1, 1))
    l_R2 = [sp.limit(k**n*sig_R2, k, sp.oo) for n in (2, 4, 8)]
    l_id4, l_id2 = sp.simplify(sp.limit(k**4*sig_R1_id, k, sp.oo)), sp.limit(k**2*sig_R1_id, k, sp.oo)
    l_maj = sp.simplify(sp.limit(k**2*sig_R1_maj, k, sp.oo))
    l_yuk = sp.simplify(sp.limit(k**4*sig_yuk/sp.log(k), k, sp.oo))
    check("C10: tails: the pair-channel gate R2 falls faster than any power (k^n sigma -> 0, n = 2, 4, 8); R1 with "
          "Gaussian profiles has power-law tails, k^4 sigma_V -> 2 pi mu^4 (identical chi), k^2 sigma_T -> 2 pi mu^2 "
          "(distinct species); Yukawa k^4 sigma_T/ln k -> pi",
          l_R2 == [0, 0, 0] and sp.simplify(l_id4 - 2*sp.pi*mu**4) == 0 and l_id2 == 0 and
          sp.simplify(l_maj - 2*sp.pi*mu**2) == 0 and l_yuk == sp.pi, f"{l_R2}, {l_id4}, {l_maj}, {l_yuk}")
    table = {0.5: ("5.081e+00", "2.058e+01", "9.246e+00", "5.817e-01"),
             2.0: ("2.810e-03", "3.492e-01", "1.473e+00", "7.947e-02"),
             5.0: ("1.616e-21", "9.852e-03", "2.488e-01", "5.772e-03"),
             10.0: ("1.159e-86", "6.252e-04", "6.267e-02", "5.694e-04")}
    bad = []
    for kk, w in table.items():
        got = tuple(f"{float(e_.subs({k: kk, mu: 1.0, Mx: 2.0})):.3e}"
                    for e_ in (sig_R2*8*sp.pi/3, sig_R1_id, sig_R1_maj, sig_yuk))
        if got != w:
            bad.append((kk, got))
    check("C10: the table at k/mu = 0.5, 2, 5, 10 reproduces (R2 sigma_V, R1 identical sigma_V, R1 distinct sigma_T, "
          "Yukawa M_X = 2 mu sigma_T); at k = 10 mu R2 gives 1.159e-86 against R1's 6.252e-4", not bad, f"{bad}")
    print(f"      [{time.time() - T_START:.1f} s]")


# ======================================================================================================
def section_polarization():
    print("\n== F. The vacuum polarization under Lorentz transformations; a preferred frame (port of "
          "derivation-gate-mechanism/polarization_lorentz.py; claims C13, C14)")
    # ======================================================================================================
    # T*M with (x^a, p_a), d = 4; Lorentz acts as L = diag(Lam, Lam^-T). omega = [[0,1],[-1,0]], eta = [[0,1],[1,0]]
    # (#1 s2), H0 = diag(g, g^-1), I = omega^-1 H, J = eta^-1 H, K = eta^-1 omega (#11 s5); Born rotation rho = I.
    rng = np.random.default_rng(1)
    Z4, I4 = np.zeros((4, 4)), np.eye(4)
    Lam = boost(rng.normal(size=3), 0.9) @ rotation(rng.normal(size=3), 1.1)
    lor = np.abs(Lam.T @ ETA @ Lam - ETA).max()
    L = np.block([[Lam, Z4], [Z4, np.linalg.inv(Lam).T]])
    Li = np.linalg.inv(L)
    omega = np.block([[Z4, I4], [-I4, Z4]])
    eta = np.block([[Z4, I4], [I4, Z4]])
    K0 = np.linalg.inv(eta) @ omega
    out = {}
    for tag, g in (("Lorentzian", ETA), ("Euclidean", np.eye(4))):
        H0 = np.block([[g, Z4], [Z4, np.linalg.inv(g)]])
        J0 = np.linalg.inv(eta) @ H0
        I0 = np.linalg.inv(omega) @ H0
        rho = I0
        out[tag] = dict(
            pd=bool(np.all(np.linalg.eigvalsh(H0) > 0)),
            alg=max(np.abs(I0 @ I0 + np.eye(8)).max(), np.abs(J0 @ J0 - np.eye(8)).max(), np.abs(K0 @ K0 - np.eye(8)).max(),
                    np.abs(I0 @ J0 - K0).max()),
            inv=[np.abs(L.T @ omega @ L - omega).max(), np.abs(L.T @ eta @ L - eta).max(), np.abs(L @ K0 @ Li - K0).max(),
                 np.abs(L @ J0 @ Li - J0).max(), np.abs(L.T @ H0 @ L - H0).max()],
            flip=[np.abs(rho @ K0 @ np.linalg.inv(rho) + K0).max(), np.abs(rho @ J0 @ np.linalg.inv(rho) + J0).max(),
                  np.abs(rho.T @ omega @ rho - omega).max()],
            rhoL=np.abs(L @ rho @ Li - rho).max())
    lo, eu = out["Lorentzian"], out["Euclidean"]
    fmt = lambda xs: ", ".join(f"{x_:.1e}" for x_ in xs)
    # round-off residuals are checked against the quoted bound (1e-15), not digit by digit: their last digits depend
    # on the linear-algebra library; the record printed 4.4e-16 and 2.5e-16, 2.5e-16, 3.2e-16, 8.9e-16, 7.8e-16
    check("C13: the boost-rotation Lam (seed 1) is Lorentz (|Lam^T g Lam - g| < 1e-15; printed 4.4e-16); the algebra "
          "I^2 = -1, J^2 = 1, K^2 = 1, IJ = K holds for Lorentzian and Euclidean g", lor < 1e-15 and
          lo['alg'] < 1e-15 and eu['alg'] < 1e-15, f"{lor:.2e}")
    check("C13: with Lorentzian g, omega, eta, K, J and H are all invariant under L = diag(Lam, Lam^-T) (residuals "
          "<= 1e-15; printed 2.5e-16, 2.5e-16, 3.2e-16, 8.9e-16, 7.8e-16), and H is not positive definite",
          max(lo['inv']) <= 1e-15 and not lo['pd'], fmt(lo['inv']))
    check("C13: the Born rotation rho = I flips K and J (rho K rho^-1 = -K, rho J rho^-1 = -J), preserves omega, and "
          "commutes with L (printed 8.9e-16): the vacuum breaks rho, not Lorentz symmetry",
          max(lo['flip']) < 1e-15 and lo['rhoL'] <= 1e-15, f"{fmt(lo['flip'])}; {lo['rhoL']:.1e}")
    check("C13: with positive-definite H (Euclidean g, as the compatibility theorem assumes) J and H are not "
          "Lorentz-invariant: |L J L^-1 - J| = 2.5, |L^T H L - H| = 2.9, |L rho L^-1 - rho| = 2.5; omega, eta, K still are",
          eu['pd'] and f"{eu['inv'][3]:.1e}" == "2.5e+00" and f"{eu['inv'][4]:.1e}" == "2.9e+00" and
          f"{eu['rhoL']:.1e}" == "2.5e+00" and max(eu['inv'][:3]) <= 1e-15 and max(eu['flip']) < 1e-15, fmt(eu['inv']))
    mV = rng.normal(size=3); kv = rng.normal(size=3); kpv = np.linalg.norm(kv)*rng.normal(size=3)
    kpv = np.linalg.norm(kv)*kpv/np.linalg.norm(kpv)
    lhs = sum(np.dot(mV + ki, mV + ki) for ki in (kv, -kv, kpv, -kpv))
    Vs = sp.Matrix(sp.symbols('V1:4', real=True)); ks = sp.Matrix(sp.symbols('ka1:4', real=True))
    kps = sp.Matrix(sp.symbols('kb1:4', real=True)); ms = sp.symbols('m', positive=True)
    tot = sum(((ms*Vs + ki).dot(ms*Vs + ki) for ki in (ks, -ks, kps, -kps)), sp.Integer(0))
    check("C14: Galilean identity sum_i |mV + k_i|^2 = 4m^2 V^2 + 2|k|^2 + 2|k'|^2 (sympy) = 4m^2V^2 + 4k^2 for "
          "|k| = |k'|; numeric (seed 1) 4.5805875967 = 4.5805875967; so a per-leg profile exp(-|p_u|^2/4mu^2) gives "
          "exp(-k^2/mu^2) exp(-m^2V^2/mu^2)",
          sp.expand(tot - 4*ms**2*Vs.dot(Vs) - 2*ks.dot(ks) - 2*kps.dot(kps)) == 0 and
          f"{lhs:.10f}" == "4.5805875967" and f"{4*mV @ mV + 4*kv @ kv:.10f}" == "4.5805875967",
          f"{lhs:.12f}, {4*mV @ mV + 4*kv @ kv:.12f}")


# ======================================================================================================
def section_run3():
    print("\n== G. Run 3's theory verifier (ports of verify-critic-theory/v3_gate_range.py, v6_medium_mediator.py; "
          "the J = 2 parts of v1_spinJ_residues.py; T3 of v7_misc_numbers.py)")
    # ======================================================================================================
    # G1 gate-range (v3). Sandwich A = F^{1/2}(p) V(x) F^{1/2}(p), the Hermitian form of #11 s8's M(k,q) = V~(q) F(k^2/mu^2);
    # hbar = mu = 1. (a) Weyl symbol of f(p) e^{iqx} g(p) is e^{iqx} f(p + q/2) g(p - q/2), so for Gaussian F the symbol
    # is F(p) times V smoothed over hbar/mu.
    p, a, mu = sp.symbols('p a mu', real=True)
    F = sp.exp(-p**2/mu**2)
    r1 = sp.simplify(sp.powsimp(sp.expand(F.subs(p, p + a)*F.subs(p, p - a)/(F*sp.exp(-a**2/mu**2))**2), force=True))
    px, py, pz, ax, ay, az = sp.symbols('px py pz ax ay az', real=True)
    F3 = lambda X, Y, Z: sp.exp(-(X**2 + Y**2 + Z**2)/mu**2)
    r3 = sp.simplify(sp.powsimp(sp.expand(F3(px + ax, py + ay, pz + az)*F3(px - ax, py - ay, pz - az)/
                                          (F3(px, py, pz)*sp.exp(-(ax**2 + ay**2 + az**2)/mu**2))**2), force=True))
    check("gate-range (a): Gaussian sandwich symbol: [sqrt(F(p+a) F(p-a))]^2/[F(p) exp(-a^2/mu^2)]^2 = 1 in 1D and 3D, "
          "so W_A(x,p) = F(p) x (V smoothed by a Gaussian of width ~hbar/mu)", r1 == 1 and r3 == 1)

    # (b) exact quantum expectation on an FFT grid vs the classical gated value
    Lbox, dx = 6000.0, 0.25
    N = int(Lbox/dx)
    x = (np.arange(N) - N//2)*dx
    kk = 2*np.pi*np.fft.fftfreq(N, d=dx)
    def expect(psi, Fhalf, V):
        phi = np.fft.ifft(Fhalf*np.fft.fft(psi))
        phi = np.fft.ifft(Fhalf*np.fft.fft(V*phi))
        return (np.vdot(psi, phi)*dx).real
    gates = {"G": lambda q: np.exp(-q**2), "L": lambda q: 1.0/(1.0 + q**2)}
    pots = {"exp": lambda X: np.exp(-np.abs(X)/300.0), "sqrt": lambda X: 1.0/np.sqrt(X**2 + 1.0)}
    X0 = [3.0, 10.0, 30.0, 100.0, 300.0, 1000.0]
    s = 6.0
    # printed (v3_gate_range.out): per (gate, V) and x0, quantum/classical-gated at p0 = 0,1,2 | quantum/ungated <V>
    printed = {
        ("G", "exp"): ["0.999903, 0.999903, 0.999903 | 0.99303, 0.37035, 0.01921",
                       "0.999974, 0.999974, 0.999974 | 0.99310, 0.37038, 0.01921"] +
                      ["1.000003, 1.000003, 1.000003 | 0.99313, 0.37039, 0.01921"]*4,
        ("G", "sqrt"): ["0.996653, 0.996653, 0.996653 | 0.98980, 0.36915, 0.01915",
                        "1.003152, 1.003152, 1.003152 | 0.99626, 0.37156, 0.01927",
                        "1.000725, 1.000725, 1.000725 | 0.99385, 0.37066, 0.01923",
                        "1.000051, 1.000051, 1.000051 | 0.99318, 0.37041, 0.01922",
                        "1.000006, 1.000006, 1.000006 | 0.99313, 0.37039, 0.01921",
                        "1.000001, 1.000001, 1.000001 | 0.99313, 0.37039, 0.01921"],
        ("L", "exp"): ["0.999906, 0.999999, 1.000012 | 0.99310, 0.50172, 0.20062",
                       "0.999974, 1.000000, 1.000003 | 0.99317, 0.50172, 0.20061"] +
                      ["1.000003, 1.000000, 1.000000 | 0.99320, 0.50172, 0.20061"]*4,
        ("L", "sqrt"): ["0.996738, 0.999965, 1.000404 | 0.98996, 0.50170, 0.20069",
                        "1.003053, 1.000038, 0.999617 | 0.99623, 0.50174, 0.20054",
                        "1.000713, 1.000006, 0.999913 | 0.99390, 0.50172, 0.20060",
                        "1.000050, 1.000000, 0.999994 | 0.99325, 0.50172, 0.20061",
                        "1.000005, 1.000000, 0.999999 | 0.99320, 0.50172, 0.20061",
                        "1.000000, 1.000000, 1.000000 | 0.99320, 0.50172, 0.20061"]}
    dev = {x0: 0.0 for x0 in X0}
    bad, supp = [], {}
    for (gname, vname), lines in printed.items():
        Fg, Vf = gates[gname], pots[vname]
        Fhalf, V = np.sqrt(Fg(kk)), Vf(x)
        for x0, line in zip(X0, lines):
            row = []
            for p0 in (0.0, 1.0, 2.0):
                psi = np.exp(-(x - x0)**2/(4*s*s) + 1j*p0*x)
                psi /= np.sqrt(np.sum(np.abs(psi)**2)*dx)
                q_exp = expect(psi, Fhalf, V)
                gx = np.exp(-(x - x0)**2/(2*s*s)); gx /= gx.sum()
                pv = np.linspace(p0 - 8/(2*s), p0 + 8/(2*s), 4001)
                gp = np.exp(-(pv - p0)**2*2*s*s); gp /= gp.sum()
                cl = np.sum(gx*V)*np.sum(gp*Fg(pv))
                row.append((q_exp/cl, q_exp/np.sum(gx*V)))
                dev[x0] = max(dev[x0], abs(q_exp/cl - 1))
            got = ", ".join(f"{r_[0]:.6f}" for r_ in row) + " | " + ", ".join(f"{r_[1]:.5f}" for r_ in row)
            if got != line:
                bad.append((gname, vname, x0, got))
            if x0 == 1000.0:
                supp[(gname, vname)] = [r_[1] for r_ in row]
    check("gate-range (b): all 72 printed ratios quantum/classical-gated and quantum/ungated reproduce (Gaussian and "
          "Lorentzian gates; V = exp(-|x|/300) and 1/sqrt(x^2 + 1); x0 = 3-1000 hbar/mu; p0 = 0, 1, 2 mu)",
          not bad, f"{bad}")
    check("gate-range (b): Gaussian gate, V = 1/sqrt(x^2 + 1): quantum/classical-gated = 0.996653, 1.003152, 1.000725, "
          "1.000051, 1.000006, 1.000001 at x0 = 3, 10, 30, 100, 300, 1000 hbar/mu: non-relativistically the gate is "
          "not tied to contact range", not any(b_[:2] == ("G", "sqrt") for b_ in bad))
    check("gate-range (b): quantum equals the classical gated value within 3.4e-3 at 3-10 hbar/mu (worst 3.35e-3), "
          "7e-4 at 30, 5e-5 at 100 (worst 5.1e-5, '1.000051'), and below 1e-5 from 300 on",
          max(dev[3.0], dev[10.0]) <= 3.4e-3 and sig(max(dev[3.0], dev[10.0]), 3) == 3.35e-3 and
          sig(dev[30.0], 1) == 7e-4 and sig(dev[100.0], 2) == 5.1e-5 and max(dev[300.0], dev[1000.0]) < 1e-5,
          ", ".join(f"{x0:g}: {d_:.2e}" for x0, d_ in dev.items()))
    sp_ = 1/(2*s)
    cfG = [exp(-p0**2/(1 + 2*sp_**2))/sqrt(1 + 2*sp_**2) for p0 in (0.0, 1.0, 2.0)]
    check("gate-range (b): the gate survives at 1000 hbar/mu: quantum/ungated = 0.99313, 0.37039, 0.01921 at p0 = 0, 1, "
          "2 mu (Gaussian; = the closed-form packet average exp(-p0^2/(1 + 2 sp^2))/sqrt(1 + 2 sp^2), sp = 1/12) and "
          "0.99320, 0.50172, 0.20061 (Lorentzian)",
          [f"{x_:.5f}" for x_ in supp[("G", "sqrt")]] == ["0.99313", "0.37039", "0.01921"] and
          [f"{x_:.5f}" for x_ in cfG] == ["0.99313", "0.37039", "0.01921"] and
          [f"{x_:.5f}" for x_ in supp[("L", "sqrt")]] == ["0.99320", "0.50172", "0.20061"] and
          max(abs(u_ - v_) for u_, v_ in zip(supp[("G", "exp")], cfG)) < 1e-5,
          ", ".join(f"{x_:.6f}" for x_ in cfG))
    # (c) 3D, Gaussian gate, Coulomb V: smoothed potential = erf(r)/r
    mp.mp.dps = 30
    worst = 0.0
    for r in (0.5, 1.0, 2.0, 3.0, 10.0):
        r = mp.mpf(r)
        val = (2/mp.pi)*mp.quad(lambda q: mp.sin(q*r)/(q*r)*mp.e**(-q*q/4), [0, mp.inf])
        worst = max(worst, float(abs(val*r - mp.erf(r))))
    check("gate-range (c): 3D Gaussian gate on Coulomb V: the smoothed potential times r equals erf(r mu/hbar) at "
          "r = 0.5, 1, 2, 3, 10 hbar/mu (0.9999779095 at 3) to 10 digits", worst < 1e-10, f"{worst:.1e}")
    # (d) record numbers in run 3's convention, v* = 120 km/s
    xg_ = (C_KMS/VSTAR_R3)**2
    n_d, n_mw = 1.0*1e3/M_CHI, 0.4*1e3/M_CHI
    check("gate-range (d): with v* = 120 km/s, mu c = m v*/sqrt2 = 19.813 keV, hbar/mu = 9.960e-12 m, "
          "x = c^2/v*^2 = 6.2414e6 = (mc/mu)^2/2",
          round(MU_R3*1e3, 3) == 19.813 and sig(HBARC/MU_R3*1e-15, 4) == 9.960e-12 and sig(xg_, 5) == 6.2414e6 and
          close(xg_, (M_CHI/MU_R3)**2/2, 1e-12), f"{MU_R3*1e3:.5f} keV, {HBARC/MU_R3*1e-15:.5e} m, {xg_:.6e}")
    check("gate-range (d): mean chi spacing n^(-1/3) = 4.121e-3 m in a dwarf core (1 GeV/cm^3, n = 14.29/cm^3) and "
          "5.593e-3 m locally (0.4 GeV/cm^3, n = 5.71/cm^3), far above hbar/mu",
          sig(n_d**(-1/3)*1e-2, 4) == 4.121e-3 and sig(n_mw**(-1/3)*1e-2, 4) == 5.593e-3 and
          round(n_d, 2) == 14.29 and round(n_mw, 2) == 5.71)

    # G2 medium or slow mediator (v6): (1/c_s^2) phi_tt - lap phi = delta^3(x - V t)
    xi, yy, zz, t, V, cs, X = sp.symbols('xi y z t V c_s x', real=True)
    r_sub = sp.sqrt((X - V*t)**2 + (1 - V**2/cs**2)*(yy**2 + zz**2))
    phi_sub = 1/(4*sp.pi*r_sub)
    pde_sub = sp.simplify(sp.diff(phi_sub, t, 2)/cs**2 - sp.diff(phi_sub, X, 2) - sp.diff(phi_sub, yy, 2) - sp.diff(phi_sub, zz, 2))
    r_sup = sp.sqrt((X - V*t)**2 - (V**2/cs**2 - 1)*(yy**2 + zz**2))
    phi_sup = 1/(2*sp.pi*r_sup)
    pde_sup = sp.simplify(sp.diff(phi_sup, t, 2)/cs**2 - sp.diff(phi_sup, X, 2) - sp.diff(phi_sup, yy, 2) - sp.diff(phi_sup, zz, 2))
    check("T6: a source moving at V through a mediator of speed c_s: the Heaviside ellipsoid "
          "1/(4 pi sqrt(xi^2 + (1 - V^2/c_s^2) rho^2)) (V < c_s) and the Mach-cone field "
          "1/(2 pi sqrt(xi^2 - (V^2/c_s^2 - 1) rho^2)) (V > c_s) solve the wave equation away from the source; "
          "V -> 0 gives Coulomb", pde_sub == 0 and pde_sup == 0 and
          sp.simplify(phi_sub.subs(V, 0) - 1/(4*sp.pi*sp.sqrt(X**2 + yy**2 + zz**2))) == 0)
    d, rho = sp.symbols('d rho', positive=True)
    bsym = sp.symbols('beta', positive=True)
    forces = {}
    for beta in (0, sp.Rational(1, 2), sp.Rational(9, 10), sp.Rational(99, 100), bsym):
        ph = 1/(4*sp.pi*sp.sqrt(xi**2 + (1 - beta**2)*rho**2))
        forces[beta] = (sp.simplify(-sp.diff(ph, rho).subs({xi: 0, rho: d})*4*sp.pi*d**2),
                        sp.simplify(sp.diff(ph, xi).subs({xi: -d, rho: 0})*4*sp.pi*d**2),
                        sp.simplify(-sp.diff(ph, xi).subs({xi: d, rho: 0})*4*sp.pi*d**2))
    sb = sp.sqrt(bsym**2 - 1)
    ph_s = 1/(2*sp.pi*sp.sqrt(xi**2 - sb**2*rho**2))
    trail_sup = sp.simplify(sp.diff(ph_s, xi).subs({xi: -d, rho: 0})*4*sp.pi*d**2)
    side = [forces[b_][0] for b_ in (sp.Rational(1, 2), sp.Rational(9, 10), sp.Rational(99, 100))]
    check("T6: two bodies at zero relative velocity, both moving at V: side by side the force is 1/sqrt(1 - V^2/c_s^2) "
          "times static, 2 sqrt3/3 = 1.155, 10 sqrt19/19 = 2.294, 100 sqrt199/199 = 7.089 at V/c_s = 1/2, 9/10, 99/100; "
          "in line it is unchanged below c_s",
          side == [2*sp.sqrt(3)/3, 10*sp.sqrt(19)/19, 100*sp.sqrt(199)/199] and
          [round(float(x_), 3) for x_ in side] == [1.155, 2.294, 7.089] and forces[0][0] == 1 and
          sp.simplify(forces[bsym][0] - 1/sp.sqrt(1 - bsym**2)) == 0 and
          all(forces[b_][1] == 1 and forces[b_][2] == 1 for b_ in forces if b_ != bsym), f"{side}")
    check("T6: above c_s the trailing body feels twice the static force (2, for any V > c_s) while the side-by-side and "
          "leading bodies, outside the cone, feel none: action and reaction are unequal, so the dependence is on "
          "velocity through the medium, not between the bodies", sp.simplify(trail_sup.subs(bsym, 2)) == 2 and
          sp.simplify(trail_sup) == 2, f"{trail_sup}")

    # G3 the J = 2 residue between point sources (v1 parts B, C, D): explicit complex on-shell q orthogonal to u1, u2
    eta = ETA.astype(complex)
    gam = 1.37
    u1 = np.array([1, 0, 0, 0], complex)
    u2 = np.array([gam, 0, 0, sqrt(gam**2 - 1)], complex)
    q_up = np.array([0, 1j, 0, 0])                                   # M = 1: q.q = M^2, q.u1 = q.u2 = 0
    q_lo = eta @ q_up
    th = eta - np.outer(q_lo, q_lo)
    TH = lambda a_, b_, t_: complex(a_ @ t_ @ b_)
    fp = TH(u1, u2, th)**2 - TH(u1, u1, th)*TH(u2, u2, th)/3
    dd = TH(u1, u2, eta)**2 - TH(u1, u1, eta)*TH(u2, u2, eta)/2
    qn = np.array([0, 1, 1j, 0])
    e_t, e_z = np.array([1, 0, 0, 0], complex), np.array([0, 0, 0, 1], complex)
    epp, epm = (e_t + e_z)/sqrt(2), (e_t - e_z)/sqrt(2)
    dotc = lambda a_, b_: complex(a_ @ eta @ b_)
    hel = (dotc(u1, epp)**2*dotc(u2, epm)**2 + dotc(u1, epm)**2*dotc(u2, epp)**2)/(2*dotc(u1, epp)**2*dotc(u1, epm)**2)
    check("c1 (J = 2, X's own residue): Fierz-Pauli contracted with point sources u1, u2 and an on-shell complex q "
          "orthogonal to both gives P_2(gamma) = (3 gamma^2 - 1)/2 = 2.315350 times static at gamma = 1.37; de Donder and "
          "the massless helicity sum give T_2(gamma) = 2 gamma^2 - 1 = 2.753800; static ratio massive/massless = 4/3",
          f"{(fp/(2/3)).real:.6f}" == "2.315350" and abs(fp/(2/3) - (3*gam**2 - 1)/2) < 1e-14 and
          f"{(dd/0.5).real:.6f}" == "2.753800" and abs(hel - (2*gam**2 - 1)) < 1e-14 and
          abs(dotc(qn, qn)) == 0 and abs(dotc(epp, qn)) == 0 and abs((2/3)/0.5 - 4/3) < 1e-15 and
          abs(TH(q_up, q_up, eta) - 1) < 1e-15,
          f"{(fp/(2/3)).real:.10f}, {(dd/0.5).real:.10f}, {hel.real:.10f}")
    beta = sp.symbols('beta', positive=True)
    gm = 1/sp.sqrt(1 - beta**2)
    cP = sp.series(sp.legendre(2, gm), beta, 0, 3).removeO().coeff(beta, 2)
    cT = sp.series(sp.chebyshevt(2, gm), beta, 0, 3).removeO().coeff(beta, 2)
    mp.mp.dps = 40
    gs = 1/mp.sqrt(1 - (mp.mpf(VSTAR_R3)/mp.mpf(C_KMS))**2)
    P2m1, T2m1 = (3*gs**2 - 1)/2 - 1, 2*gs**2 - 2
    check("c1 (J = 2): the (v/c)^2 coefficients are J(J+1)/4 = 3/2 (massive X) and J^2/2 = 2 (massless graviton); at "
          "v_rel = 120 km/s P_2(gamma) - 1 = 2.40332e-7 and T_2(gamma) - 1 = 3.20443e-7",
          cP == sp.Rational(3, 2) and cT == 2 and mp.nstr(P2m1, 6) == "2.40332e-7" and mp.nstr(T2m1, 6) == "3.20443e-7",
          f"{mp.nstr(P2m1, 10)}, {mp.nstr(T2m1, 10)}")

    # G4 T3 (v7): the velocity scale of gravitational ladder (Bohr-type) effects between chi quanta
    m_kg = M_CHI*1e6*EV/C**2
    aG = G_N*m_kg**2/(HBAR*C)
    check("T3: for gravitational-strength exchange between 70 MeV chi, alpha_G = G m^2/(hbar c) = 3.287e-41 and the "
          "Bohr-type velocity alpha_G c = 9.855e-33 m/s: loops bring no scale near v* either",
          sig(aG, 4) == 3.287e-41 and sig(aG*C, 4) == 9.855e-33, f"{aG:.6e}, {aG*C:.6e} m/s")
    print(f"      [{time.time() - T_START:.1f} s]")
    return dict(side_half=float(side[0]))


# ======================================================================================================
def section_side_by_side(B, G):
    print("\n== H. The two derivations side by side (quantities both computed)")
    # ======================================================================================================
    m, k = B['m'], B['k']
    gamma = sp.symbols('gamma')
    p1, p2, p3, p4 = B['p']
    gam_cm = sp.simplify(sp.expand((B['eta']*p1).T*p2)[0, 0]/m**2)
    P2g = sp.expand(((3*gamma**2 - 1)/2).subs(gamma, gam_cm))
    check("H1: run 4's forward numerator N_min(k,0)/N_min(0,0) = 1 + 6k^2/m^2 + 6k^4/m^4 is exactly run 3's spin-2 "
          "residue P_2(gamma) with gamma = p1.p2/m^2 = 1 + 2k^2/m^2", sp.simplify(gam_cm - (1 + 2*k**2/m**2)) == 0 and
          sp.expand(P2g - B['fwd']) == 0, f"gamma = {gam_cm}")
    M, s_, u_, t_ = B['M'], B['s'], B['u'], B['t']
    pdot12 = sp.expand((B['eta']*p1).T*p2)[0, 0]
    zt = (4*m**2*gamma + M**2)/(4*m**2 - M**2)
    check("H2: s - u = 4 p1.p2 + t, so run 4's pole variable z_t = (s - u)/(4m^2 - M_X^2) at t = M_X^2 is "
          "(4m^2 gamma + M_X^2)/(4m^2 - M_X^2) -> gamma as M_X/m -> 0: run 4's residue P_2(z_t) becomes run 3's P_2(gamma)",
          sp.simplify(s_ - u_ - 4*pdot12 - t_) == 0 and
          sp.simplify(B['Ssub']/(4*m**2 - M**2) - zt.subs(gamma, gam_cm)) == 0 and sp.limit(zt, M, 0) == gamma)
    kk = VSTAR_R3/(2*C_KMS)
    r4v = 6*kk**2 + 6*kk**4
    gs = 1/sqrt(1 - (VSTAR_R3/C_KMS)**2)
    r3v = (3*gs**2 - 1)/2 - 1
    check("H3: X's velocity dependence at 120 km/s: run 4 (forward numerator, k = m v/2) 2.4033e-7 and run 3 "
          "(P_2(gamma) - 1, relativistic gamma) 2.40332e-7 agree to the quoted digits (they differ at O(v^4/c^4))",
          sig(r4v, 5) == 2.4033e-7 and sig(r3v, 6) == 2.40332e-7 and abs(r4v/r3v - 1) < 1e-6,
          f"{r4v:.8e} vs {r3v:.8e}, relative difference {abs(r4v/r3v - 1):.1e}")
    # the massless (de Donder) numerator with run 4's minimal vertices at k = q = 0
    vertex, fmin, c = B['vertex'], B['fmin'], B['c']
    V1 = vertex(p1, p3, fmin).subs({k: 0, c: 1})
    V2 = vertex(p2, p4, fmin).subs({k: 0, c: 1})
    eta = B['eta']
    Nmassless = sp.simplify((V1*eta*V2*eta).trace() - sp.Rational(1, 2)*(V1*eta).trace()*(V2*eta).trace())
    check("H4: vDVZ in both: run 4's N_min(0,0) = 8m^4/3 against the massless (de Donder) numerator 2m^4 for the same "
          "vertices is 4/3, run 3's static ratio massive/massless 1.333333",
          sp.simplify(Nmassless - 2*m**4) == 0 and sp.simplify(B['N00']/Nmassless - sp.Rational(4, 3)) == 0,
          f"massless {Nmassless}")
    check("H5: the gate's nonlocality hbar/mu: run 4 9.87 pm (mu c = 20 keV), run 3 9.960 pm (v* = 120 km/s); they "
          "differ by 0.95%, exactly the ratio of the two readings of the record's mu = m v*/sqrt2 ~ 20 keV "
          "(121.1/120 km/s)", round(HBARC/MU_R4/1e3, 2) == 9.87 and round(HBARC/MU_R3/1e3, 2) == 9.96 and
          close((HBARC/MU_R3)/(HBARC/MU_R4), VSTAR_R4/VSTAR_R3, 1e-12) and round(100*(MU_R4/MU_R3 - 1), 2) == 0.95,
          f"{HBARC/MU_R4/1e3:.4f} vs {HBARC/MU_R3/1e3:.4f} pm, ratio {MU_R4/MU_R3:.6f}")
    check("H6: (m c/mu)^2: run 4 1.225e7 (mu c = 20 keV), run 3 2x = 2 c^2/v*^2 = 1.248e7 (v* = 120 km/s): the same "
          "quantity in the two conventions, ratio (121.1/120)^2 = 1.019",
          sig((M_CHI/MU_R4)**2, 4) == 1.225e7 and sig(2*(C_KMS/VSTAR_R3)**2, 4) == 1.248e7 and
          close(2*(C_KMS/VSTAR_R3)**2/(M_CHI/MU_R4)**2, (VSTAR_R4/VSTAR_R3)**2, 1e-12),
          f"{(M_CHI/MU_R4)**2:.5e}, {2*(C_KMS/VSTAR_R3)**2:.5e}")
    n1, n2 = B['n1'], B['n2']
    F1 = sp.Symbol('F1')
    check("H7: both find that spin-2 exchange grows with relative velocity and never gates: run 4's forward coefficients "
          "n1 = 64 F1^2 m^2, n2 = 64 F1^2 are >= 0 for real F1; run 3's P_2'(gamma) = 3 gamma > 0 for gamma >= 1",
          sp.simplify(n1.subs(F1, sp.Symbol('f', real=True))).is_nonnegative and
          sp.simplify(n2.subs(F1, sp.Symbol('f', real=True))).is_nonnegative and
          sp.diff((3*gamma**2 - 1)/2, gamma) == 3*gamma)
    check("H8: both find a preferred frame (medium, slow mediator, or Lorentz-violating vertex) gives dependence on "
          "velocity through that frame at zero relative velocity, not on relative velocity: run 4's factor at k = 0, "
          "V = 300 km/s is exp(-m^2V^2/mu^2) = 4.7e-6; run 3's side-by-side force at V = c_s/2 is 1.155 times static",
          sig(exp(-2*300**2/VSTAR_R4**2), 2) == 4.7e-6 and round(G['side_half'], 3) == 1.155)


# ======================================================================================================
section_anchors()
B = section_tchannel()
section_fermion()
section_numbers()
section_fiber()
section_polarization()
G = section_run3()
section_side_by_side(B, G)

# ======================================================================================================
print(f"\nwall time {time.time() - T_START:.1f} s")
if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — every result of the gate-mechanism derivation reproduces.")
