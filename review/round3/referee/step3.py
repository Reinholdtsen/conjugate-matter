"""Step 3: compatibility theorem. omega = [[0,1],[-1,0]], eta = [[0,1],[1,0]] (d x d blocks), H = [[A,C],[C^T,B]].
Conditions: (eta^-1 H)^2 = 1 and (omega^-1 H)^2 = -1. Claim: H positive => C=0, B=A^-1."""
import sympy as sp
import numpy as np

def blocks(d):
    I = sp.eye(d); Z = sp.zeros(d)
    omega = sp.BlockMatrix([[Z, I], [-I, Z]]).as_explicit()
    eta = sp.BlockMatrix([[Z, I], [I, Z]]).as_explicit()
    return omega, eta

def sym_mat(name, d, symmetric):
    if symmetric:
        s = sp.symbols(f"{name}0:{d*(d+1)//2}")
        M = sp.zeros(d); k = 0
        for i in range(d):
            for j in range(i, d):
                M[i, j] = M[j, i] = s[k]; k += 1
        return M, list(s)
    s = sp.symbols(f"{name}0:{d*d}")
    return sp.Matrix(d, d, s), list(s)

for d in [1, 2]:
    print(f"\n===== d = {d} (symbolic) =====")
    omega, eta = blocks(d)
    A, sa = sym_mat("a", d, True); B, sb = sym_mat("b", d, True); C, sc = sym_mat("c", d, False)
    H = sp.BlockMatrix([[A, C], [C.T, B]]).as_explicit()
    E1 = sp.expand((eta.inv() * H)**2 - sp.eye(2*d))
    E2 = sp.expand((omega.inv() * H)**2 + sp.eye(2*d))
    # check the manuscript's block identities
    b21_1 = E1[d:, :d]; b21_2 = E2[d:, :d]
    print("(2,1) block of (eta^-1 H)^2 - 1 == A C^T + C A :", sp.simplify(b21_1 - (A*C.T + C*A)) == sp.zeros(d))
    print("(2,1) block of (omega^-1 H)^2 + 1 == C A - A C^T :", sp.simplify(b21_2 - (C*A - A*C.T)) == sp.zeros(d))
    print("sum = 2 C A :", sp.simplify(b21_1 + b21_2 - 2*C*A) == sp.zeros(d), "; difference = 2 A C^T :", sp.simplify(b21_1 - b21_2 - 2*A*C.T) == sp.zeros(d))
    # with C = 0 the remaining equations reduce to B A = 1
    sub0 = {c: 0 for c in sc}
    E1c, E2c = E1.subs(sub0), E2.subs(sub0)
    print("with C=0: (1,1) block of E1 == B A - 1 :", sp.simplify(E1c[:d, :d] - (B*A - sp.eye(d))) == sp.zeros(d),
          "; (2,2) block == A B - 1 :", sp.simplify(E1c[d:, d:] - (A*B - sp.eye(d))) == sp.zeros(d),
          "; E2 off-diag zero:", sp.simplify(E2c[:d, d:]) == sp.zeros(d) and sp.simplify(E2c[d:, :d]) == sp.zeros(d))
    # full solution set of the polynomial system (no positivity)
    eqs = list(set([e for e in list(E1) + list(E2) if e != 0]))
    sols = sp.solve(eqs, sa + sb + sc, dict=True)
    print(f"number of solution branches (no positivity imposed): {len(sols)}")
    for s in sols:
        Hs = H.subs(s)
        Cs = C.subs(s)
        # positivity test: leading principal minors / A block
        As = A.subs(s)
        print("  branch: C =", list(Cs), "| A =", list(As), "| B =", list(B.subs(s)))

# ---------------------------------------------------------------- numerical, d = 3, 4
rng = np.random.default_rng(20261019)
def omega_eta(d):
    I = np.eye(d); Z = np.zeros((d, d))
    return np.block([[Z, I], [-I, Z]]), np.block([[Z, I], [I, Z]])
def resid(H, d):
    om, et = omega_eta(d)
    r1 = np.linalg.norm(np.linalg.matrix_power(np.linalg.solve(et, H), 2) - np.eye(2*d))
    r2 = np.linalg.norm(np.linalg.matrix_power(np.linalg.solve(om, H), 2) + np.eye(2*d))
    return r1, r2
def spd(d):
    M = rng.normal(size=(d, d)); return M @ M.T + 0.5*np.eye(d)
for d in [3, 4]:
    print(f"\n===== d = {d} (numerical, 2000 trials per family) =====")
    # (a) diag(g, g^-1)
    r = np.array([resid(np.block([[g, np.zeros((d, d))], [np.zeros((d, d)), np.linalg.inv(g)]]), d) for g in (spd(d) for _ in range(2000))])
    print(f"(a) diag(g,g^-1): max residuals eta={r[:,0].max():.2e}, omega={r[:,1].max():.2e}; det H = 1 check: "
          f"{abs(np.linalg.det(np.block([[spd(d)*0+np.eye(d)*2, np.zeros((d,d))],[np.zeros((d,d)), np.eye(d)/2]]))-1):.1e}")
    # (b) generic SPD H with C != 0
    mins = []
    for _ in range(2000):
        M = rng.normal(size=(2*d, 2*d)); H = M @ M.T + 0.1*np.eye(2*d)
        mins.append(max(resid(H, d)))
    print(f"(b) generic SPD H (C!=0): min over trials of max(eta,omega residual) = {min(mins):.3f}  -> every trial violates at least one")
    # (c) eta-compatible only: O(d,d) generalized metric with B-field (C != 0)
    rr = []
    for _ in range(2000):
        g = spd(d); Bf = rng.normal(size=(d, d)); Bf = Bf - Bf.T; gi = np.linalg.inv(g)
        H = np.block([[g - Bf @ gi @ Bf, Bf @ gi], [-gi @ Bf, gi]])
        assert np.all(np.linalg.eigvalsh((H+H.T)/2) > 0)
        rr.append(resid(H, d))
    rr = np.array(rr)
    print(f"(c) eta-only family (B-field): eta residual max {rr[:,0].max():.2e}; omega residual min {rr[:,1].min():.3f}")
    # (d) omega-compatible only: Siegel parametrisation with X != 0
    rr = []
    for _ in range(2000):
        Y = spd(d); X = rng.normal(size=(d, d)); X = (X + X.T)/2; Yi = np.linalg.inv(Y)
        H = np.block([[Yi, Yi @ X], [X @ Yi, Y + X @ Yi @ X]])
        assert np.all(np.linalg.eigvalsh((H+H.T)/2) > 0)
        rr.append(resid(H, d))
    rr = np.array(rr)
    print(f"(d) omega-only family (Siegel X!=0): omega residual max {rr[:,1].max():.2e}; eta residual min {rr[:,0].min():.3f}")
    # (e) small perturbation of diag(g,g^-1) by C = delta
    g = spd(d); gi = np.linalg.inv(g)
    for eps in [1e-2, 1e-4]:
        Cp = eps*rng.normal(size=(d, d))
        H = np.block([[g, Cp], [Cp.T, gi]])
        print(f"(e) diag + C of size {eps:.0e}: residuals eta={resid(H,d)[0]:.2e}, omega={resid(H,d)[1]:.2e}")
