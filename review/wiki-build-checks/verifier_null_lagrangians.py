# Verifier scratch check (not a wiki result). Question: with standard omega and eta on R^{2d},
# are the subspaces that are both omega-Lagrangian and eta-null a discrete set (#5 §B: "discrete -
# the 2^d coordinate-type splittings")? Test d = 2 and d = 3 with L = V (+) V^perp, V a k-plane in R^d,
# moved continuously; also compute the Maslov phase det^2 along the family.
import numpy as np
rng = np.random.default_rng(7)
def forms(d):
    Z = np.zeros((d, d)); I = np.eye(d)
    return np.block([[Z, I], [-I, Z]]), np.block([[Z, I], [I, Z]])
def L_of(Q, k):
    # Q orthogonal d x d; V = span of first k columns, V^perp = span of the rest (placed in p-space)
    d = Q.shape[0]
    cols = [np.concatenate([Q[:, i], np.zeros(d)]) for i in range(k)]
    cols += [np.concatenate([np.zeros(d), Q[:, i]]) for i in range(k, d)]
    return np.column_stack(cols)
for d in (2, 3):
    om, et = forms(d)
    A = rng.standard_normal((d, d)); Askew = A - A.T          # generator of a rotation path
    for k in range(1, d):
        worst_om = worst_et = 0.0; phases = []; dist = []
        L0 = L_of(np.eye(d), k)
        for t in np.linspace(0.0, 1.0, 11):
            w, V = np.linalg.eigh(-Askew @ Askew)                  # build Q(t) = expm(t*Askew) via eig
            ev, EV = np.linalg.eig(Askew)
            Q = np.real(EV @ np.diag(np.exp(t * ev)) @ np.linalg.inv(EV))
            L = L_of(Q, k)
            worst_om = max(worst_om, np.abs(L.T @ om @ L).max())
            worst_et = max(worst_et, np.abs(L.T @ et @ L).max())
            U = L[:d, :] + 1j * L[d:, :]
            phases.append(np.linalg.det(U) ** 2)
            # distance between projectors onto L(t) and L(0): nonzero means the subspace actually moved
            P = L @ L.T; P0 = L0 @ L0.T
            dist.append(np.linalg.norm(P - P0))
        print(f"d={d} k={k}: max|omega on L|={worst_om:.1e}  max|eta on L|={worst_et:.1e}  "
              f"projector distance from t=0 up to {max(dist):.3f}  det^2 values {sorted(set(np.round(phases, 9)))}")
