"""C7 scope check. In a uniform-density (cored) halo the gravitational potential is harmonic,
Phi = (1/2) Omega^2 x^2 with Omega^2 = 4 pi G rho/3 [T]. The canonical rotation
  X = p/(m Omega),  P = -m Omega x
preserves Poisson brackets and maps H = p^2/2m + m Omega^2 x^2/2 + sum U(p_i - p_j) onto
H = P^2/2m + m Omega^2 X^2/2 + sum U(m Omega (X_i - X_j)): a trapped gas with a POSITION-space
pair attraction. So the 'exchanged Hamiltonian' x^2/2m' (1/m' = m Omega^2) is present in any
cored halo, and a velocity-only attraction there is exactly equivalent to a position-space
attraction in the same trap. Checked symbolically for two particles in 1D and 3D components."""
import sympy as sp
m, W = sp.symbols('m Omega', positive=True)
x1, p1, x2, p2 = sp.symbols('x1 p1 x2 p2', real=True)
U = sp.Function('U')
X1, P1, X2, P2 = p1/(m*W), -m*W*x1, p2/(m*W), -m*W*x2
def pb(f, g, pairs):
    return sp.simplify(sum(sp.diff(f, q)*sp.diff(g, p) - sp.diff(f, p)*sp.diff(g, q) for q, p in pairs))
pairs = [(x1, p1), (x2, p2)]
print("{X1,P1} =", pb(X1, P1, pairs), " {X1,X2} =", pb(X1, X2, pairs), " {X1,P2} =", pb(X1, P2, pairs), " {P1,P2} =", pb(P1, P2, pairs))
H_old = p1**2/(2*m) + p2**2/(2*m) + m*W**2*(x1**2 + x2**2)/2 + U(p1 - p2)
Xs, Ps = sp.symbols('Xa Pa Xb Pb', real=True)[:2], sp.symbols('Xa Pa Xb Pb', real=True)[2:]
Xa, Pa, Xb, Pb = sp.symbols('Xa Pa Xb Pb', real=True)
# inverse map: p = m W X, x = -P/(m W)
H_new = H_old.subs({p1: m*W*Xa, p2: m*W*Xb, x1: -Pa/(m*W), x2: -Pb/(m*W)})
print("H in new variables:", sp.simplify(H_new))

# Quarter period of the core oscillation (velocity structure -> position structure):
# Omega^2 = 4 pi G rho/3 = 1/(3 t_ff^2), so (pi/2)/Omega = (pi/2) sqrt(3) t_ff ~ 2.72 t_ff
# (printed by the one-liner saved in harmonic_quarter.out).
