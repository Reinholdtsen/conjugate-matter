"""Flag 39 audit, part 3: toy model I (papers/reciprocity-toy-models.md sec 2), d = 1.

Symmetries as the toy note states them: H -> S^T H S, K -> S^-1 K S for S in Sp(2,R),
plus the separate flip K -> -K.  Vacuum (H, K) = (1, K0), K0 = diag(1, -1).
1. Find every element of Sp(2,R) x {1, flip} that fixes the vacuum. (S^T S = 1 forces
   S = R(theta) in SO(2); then S^-1 K0 S = +K0 or -K0.)
2. For each, print its linear action on the fluctuations (dX, dY) of Z = X + iY at Z = i
   (H = H(Z) as in the toy note) and on the tangent (db, dc) of the K-hyperboloid at K0.
If every vacuum-preserving element acts on (dX, dY) as +1 or as -1, then no unbroken
symmetry of the program's explicit model gives the metric component dY a parity
different from dX.
"""
import sympy as sp

th = sp.symbols("theta", real=True)
R = sp.Matrix([[sp.cos(th), sp.sin(th)], [-sp.sin(th), sp.cos(th)]])
K0 = sp.diag(1, -1)
sols = {}
for sign in (+1, -1):
    eqs = [sp.simplify(e) for e in (R.inv() * K0 * R - sign * K0)]
    s = sp.solveset(sp.Eq(eqs[0], 0) & sp.Eq(eqs[1], 0), th, sp.Interval.Ropen(0, 2 * sp.pi)) \
        if False else None
    # solve componentwise on [0, 2pi)
    cand = set()
    for e in eqs:
        if e != 0:
            cand |= set(sp.solveset(e, th, sp.Interval.Ropen(0, 2 * sp.pi)))
    good = [c for c in sorted(cand, key=lambda z: float(z))
            if all(sp.simplify(e.subs(th, c)) == 0 for e in eqs)]
    sols[sign] = good
print("1. R(theta)^-1 K0 R(theta) = +K0 at theta =", sols[+1], "; = -K0 at theta =", sols[-1])

X, Y = sp.symbols("X Y", real=True)


def H_of(X, Y):
    return sp.Matrix([[Y + X**2 / Y, X / Y], [X / Y, 1 / Y]])


def Z_of(H):
    Yp = 1 / H[1, 1]
    return sp.simplify(H[0, 1] * Yp), sp.simplify(Yp)


eps = sp.symbols("eps", real=True)
dx, dy, db, dc = sp.symbols("dx dy db dc", real=True)
print("2. vacuum-preserving elements and their linear actions:")
for sign, thetas in sols.items():
    for t in thetas:
        S = R.subs(th, t)
        Hn = S.T * H_of(eps * dx, 1 + eps * dy) * S
        Xp, Yp = Z_of(Hn)
        lin = [sp.simplify(sp.diff(q, eps).subs(eps, 0)) for q in (Xp, Yp - 1)]
        # K tangent at K0 on the hyperboloid a^2 + bc = 1: dK = [[0, db], [dc, 0]]
        dK = sp.Matrix([[0, db], [dc, 0]])
        dKp = sign * (S.inv() * dK * S)
        name = ("S = R(%s)" % t) + ("" if sign == 1 else " with K -> -K")
        print(f"   {name:28s}: (dX, dY) -> ({lin[0]}, {lin[1]});  (db, dc) -> ({sp.simplify(dKp[0, 1])}, {sp.simplify(dKp[1, 0])})"
              f";  dK diagonal stays 0: {sp.simplify(dKp[0, 0]) == 0 and sp.simplify(dKp[1, 1]) == 0}")
rho = sp.Matrix([[0, 1], [-1, 0]])
print("3. rho = R(pi/2):", sp.simplify(R.subs(th, sp.pi / 2) - rho) == sp.zeros(2, 2))
