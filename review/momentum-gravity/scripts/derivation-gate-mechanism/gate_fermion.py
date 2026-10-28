#!/usr/bin/env python3
"""Dirac-fermion chi: t-channel massive spin-2 exchange, k-dependence at fixed transfer q.

Vertex chi(p_in, s_in) -> chi(p_out, s_out) + X:
  V^{mn} = (1/4) ubar_out [g^m P^n + g^n P^m] u_in                       (stress-tensor coupling)
         + kappa/(4m) ubar_out [i sigma^{m a} l_a P^n + (m<->n)] u_in       (a second, magnetic-type structure)
P = p_in + p_out, l = p_in - p_out.  Units hbar = c = 1, m = 1, metric (+,-,-,-), Dirac representation.
Prints the relative change of the amplitude with k at fixed q, divided by k^2/m^2: if the
k-dependence had a scale mu << m this ratio would be of order (m/mu)^2, not of order 1.
"""
import numpy as np

m, M = 1.0, 0.5
eta = np.diag([1.0, -1.0, -1.0, -1.0])
I2, Z2 = np.eye(2), np.zeros((2, 2))
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
gam = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in sig]
gam0 = gam[0]


def spinor(p, xi):
    E = p[0]
    sp_ = sum(p[i + 1] * sig[i] for i in range(3))
    return np.concatenate([np.sqrt(E + m) * xi, (sp_ @ xi) / np.sqrt(E + m)])


def bar(u):
    return u.conj() @ gam0


def vertex(pin, pout, uin, uout, kappa):
    P, l = pin + pout, pin - pout
    l_low = eta @ l
    V = np.zeros((4, 4), complex)
    for a in range(4):
        for b in range(4):
            V[a, b] = 0.25 * bar(uout) @ (gam[a] * P[b] + gam[b] * P[a]) @ uin
            if kappa:
                for (x, y) in ((a, b), (b, a)):
                    sxl = sum(0.5j * (gam[x] @ gam[al] - gam[al] @ gam[x]) * l_low[al] for al in range(4))
                    V[a, b] += kappa / (4 * m) * bar(uout) @ (1j * sxl * P[y]) @ uin
    return V


def spin2(V1, V2, l):
    ll = eta @ l
    G = eta - np.outer(ll, ll) / M**2
    T1 = np.trace(V1.T @ G @ V2 @ G)
    T2 = np.trace(V1 @ G @ V2 @ G)
    return 0.5 * (T1 + T2) - np.trace(V1 @ G) * np.trace(V2 @ G) / 3.0


def amp(k, q, kappa, spins):
    c = 1 - q**2 / (2 * k**2)
    s = np.sqrt(max(0.0, 1 - c**2))
    E = np.sqrt(m**2 + k**2)
    p1, p2 = np.array([E, k, 0, 0]), np.array([E, -k, 0, 0])
    p3, p4 = np.array([E, k * c, k * s, 0]), np.array([E, -k * c, -k * s, 0])
    up, dn = np.array([1, 0], complex), np.array([0, 1], complex)
    xi = {'u': up, 'd': dn}
    s1, s2, s3, s4 = (xi[ch] for ch in spins)
    V1 = vertex(p1, p3, spinor(p1, s1), spinor(p3, s3), kappa)
    V2 = vertex(p2, p4, spinor(p2, s2), spinor(p4, s4), kappa)
    return spin2(V1, V2, p1 - p3)


for q, ks in ((2e-3, [1.2e-3, 3e-3, 1e-2, 3e-2, 1e-1]), (0.1, [0.06, 0.1, 0.2, 0.3])):
    print("=== q/m = %g ===" % q)
    for kappa in (0.0, 0.7):
        for spins in ('uuuu', 'udud', 'uudd'):
            A0 = amp(ks[0], q, kappa, spins)
            rows = []
            for kk in ks[1:]:
                A = amp(kk, q, kappa, spins)
                rows.append((kk, abs(A) / abs(A0) - 1, (abs(A) / abs(A0) - 1) / ((kk**2 - ks[0]**2) / m**2)))
            print("kappa = %.1f spins %s : |A(k0 = %g)| = %.6g" % (kappa, spins, ks[0], abs(A0)))
            for kk, rel, ratio in rows:
                print("   k/m = %-7.3g  |A(k)|/|A(k0)| - 1 = %-11.4e  divided by (k^2-k0^2)/m^2 = %.4f" % (kk, rel, ratio))
