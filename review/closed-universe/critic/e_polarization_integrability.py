"""Critic, tension (e): integrability of the program's polarizations on T*S^3 (closed) and T*T^3 (flat).

Setting [D]: T*S^3 in the left trivialization S^3 x R^3 (S^3 = SU(2) of radius R, left-invariant
orthonormal frame e_a with [e_a, e_b] = (2/R) eps_abc e_c; p_a = alpha(e_a)). A vector field is
V = A^a(p) e~_a + B_a(p) d/dp_a (homogeneous: coefficients depend on p only; e~_a kills functions of p).
Liouville form lambda = p_a theta^a, omega = d lambda = dp_a ^ theta^a + p_a d theta^a,
d theta^a(e_b, e_c) = -(2/R) eps_abc.  Levi-Civita horizontal lift (bi-invariant metric):
H_a = e~_a + (1/R) eps_acb p_b d/dp_c.  Flat T^3: same with R -> infinity (structure constants 0).

The program's U(1) family of polarizations (toy note: polarization is a Goldstone angle theta):
L_theta = span{ cos(theta) d/dp_a + sin(theta) ell H_a } (ell a constant converting units).
theta = 0: vertical = x-polarization (wavefunctions of x); theta = pi/2: horizontal = p-polarization
(the mirror). Each L_theta is Lagrangian. Integrability (Frobenius): [L_a, L_b] in span L.
"""
import sympy as sp

Rr, ell, th = sp.symbols('R ell theta', positive=True)
p = sp.symbols('p1 p2 p3', real=True)
eps = sp.LeviCivita

def bracket(V, W, Rinv):
    """V = (A, B): A = base components (3), B = fibre components (3), functions of p."""
    A, B = V; C, D = W
    der = lambda Bvec, f: sum(Bvec[i]*sp.diff(f, p[i]) for i in range(3))
    base = [sum(A[a_]*C[b_]*2*Rinv*eps(a_, b_, c_) for a_ in range(3) for b_ in range(3))
            + der(B, C[c_]) - der(D, A[c_]) for c_ in range(3)]
    fib = [der(B, D[c_]) - der(D, B[c_]) for c_ in range(3)]
    return ([sp.simplify(x) for x in base], [sp.simplify(x) for x in fib])

def omega(V, W, Rinv):
    A, B = V; C, D = W
    val = sum(B[a_]*C[a_] - D[a_]*A[a_] for a_ in range(3))
    val += -2*Rinv*sum(p[d_]*eps(b_, c_, d_)*A[b_]*C[c_] for b_ in range(3) for c_ in range(3) for d_ in range(3))
    return sp.simplify(val)

def horizontal(a_, Rinv):
    A = [1 if i == a_ else 0 for i in range(3)]
    B = [Rinv*sum(eps(a_, c_, b_)*p[b_] for b_ in range(3)) for c_ in range(3)]
    return (A, B)

def vertical(a_):
    return ([0, 0, 0], [1 if i == a_ else 0 for i in range(3)])

def comb(cv, V, ch, Hh):
    return ([cv*V[0][i] + ch*Hh[0][i] for i in range(3)], [cv*V[1][i] + ch*Hh[1][i] for i in range(3)])

for label, Rinv in [('S^3 (radius R)', 1/Rr), ('flat T^3', 0)]:
    print(f"=== {label} ===")
    Hs = [horizontal(a_, Rinv) for a_ in range(3)]
    Vs = [vertical(a_) for a_ in range(3)]
    # Lagrangian checks
    lagH = all(omega(Hs[i], Hs[j], Rinv) == 0 for i in range(3) for j in range(3))
    print("  horizontal distribution Lagrangian:", lagH)
    hb = bracket(Hs[0], Hs[1], Rinv)
    print("  [H_1, H_2] =", hb[0], "e~ +", hb[1], "d/dp")
    Ls = [comb(sp.cos(th), Vs[a_], sp.sin(th)*ell, Hs[a_]) for a_ in range(3)]
    Ps = [comb(-sp.sin(th), Vs[a_], sp.cos(th)*ell, Hs[a_]) for a_ in range(3)]   # complement
    lagL = all(sp.simplify(omega(Ls[i], Ls[j], Rinv)) == 0 for i in range(3) for j in range(3))
    print("  every L_theta Lagrangian:", lagL)
    # decompose [L_1, L_2] on the frame {L_a, P_a}; non-integrability = the P components
    br = bracket(Ls[0], Ls[1], Rinv)
    cL = sp.symbols('cL1:4'); cP = sp.symbols('cP1:4')
    eqs = []
    for i in range(3):
        eqs.append(sp.Eq(br[0][i], sum(cL[a_]*Ls[a_][0][i] + cP[a_]*Ps[a_][0][i] for a_ in range(3))))
        eqs.append(sp.Eq(br[1][i], sum(cL[a_]*Ls[a_][1][i] + cP[a_]*Ps[a_][1][i] for a_ in range(3))))
    sol = sp.solve(eqs, list(cL) + list(cP), dict=True)[0]
    offL = [sp.simplify(sol[c_]) for c_ in cP]
    print("  [L_1, L_2] components outside L_theta (along the complement P_a):")
    for i, x in enumerate(offL):
        print(f"     P_{i+1}: {sp.factor(x)}")
    zero_at = {name: all(sp.simplify(x.subs(th, val)) == 0 for x in offL)
               for name, val in [('theta = 0 (x)', 0), ('theta = pi/4', sp.pi/4), ('theta = pi/2 (mirror p)', sp.pi/2)]}
    print("  integrable at:", zero_at)
    print()

print("Result: the only out-of-L component is ell^2 p sin(theta)^3 / R^2 -- the curvature of S^3 times sin^3(theta).")
print("The 2/R term of [H_1, H_2] lies inside L. So within the Born-rotation family L_theta = e^{theta I}(vertical)")
print("only theta = 0 (and theta = pi, the same plane) is integrable on T*S^3; on T^3 every theta is.")
import math
c = 299792458.0; Mpc = 3.0856775814913673e22; cH0 = c/(67.4e3/Mpc)
for Ok in [1e-2, 1e-5]:
    R0 = cH0/math.sqrt(Ok)
    for L in [1.0, 1.5e26]:
        print(f"  |Omega_k| = {Ok:.0e}: curvature measure (L/R0)^2 for L = {L:.1e} m: {(L/R0)**2:.3e}")
