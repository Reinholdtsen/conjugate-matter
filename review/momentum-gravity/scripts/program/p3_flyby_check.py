#!/usr/bin/env python3
"""Validation of the flyby integrator in p3_momentum_mechanics.py: beta = 0 must give Rutherford; step-size halving;
and the role of the anomalous velocity (switch it off while keeping the gated force) at v_inf = 0.1."""
import numpy as np
def make_rhs(beta, anomalous=True):
    def rhs(y):
        x, yy, px, py = y
        r = np.hypot(x, yy); p2 = px*px + py*py; gate = np.exp(-p2)
        fac = 1.0 + (2.0*beta*gate/r if anomalous else 0.0)
        k = (1.0 + beta*gate)/r**3
        return np.array([px*fac, py*fac, -k*x, -k*yy])
    return rhs
def rk4(rhs, y, dt):
    k1 = rhs(y); k2 = rhs(y + 0.5*dt*k1); k3 = rhs(y + 0.5*dt*k2); k4 = rhs(y + dt*k3)
    return y + dt*(k1 + 2*k2 + 2*k3 + k4)/6
def kepler_dir(y, k, outgoing):
    x, yy, px, py = y
    r = np.hypot(x, yy); L = x*py - yy*px
    A = np.array([py*L, -px*L]) - k*np.array([x, yy])/r
    e = np.hypot(*A)/k; phiA = np.arctan2(A[1], A[0]); psi = np.arccos(-1.0/e); s = 1 if L > 0 else -1
    return phiA + s*psi if outgoing else phiA - s*psi
def flyby(beta, vinf, b=20.0, R0=2.0e4, h=2e-3, anomalous=True):
    rhs = make_rhs(beta, anomalous); y = np.array([-R0, b, vinf, 0.0])
    phi_in = kepler_dir(y, 1.0 + beta*np.exp(-vinf**2), False)
    rp = 1e300
    while True:
        r = np.hypot(y[0], y[1]); rp = min(rp, r)
        y = rk4(rhs, y, h*r/max(np.hypot(y[2], y[3]), 1e-3))
        if np.hypot(y[0], y[1]) > R0 and y[0]*y[2] + y[1]*y[3] > 0:
            break
    phi_out = kepler_dir(y, 1.0 + beta*np.exp(-(y[2]**2 + y[3]**2)), True)
    return abs((phi_out - (phi_in + np.pi) + np.pi) % (2*np.pi) - np.pi), rp
for vinf in [0.1, 0.3, 1.0]:
    th0, _ = flyby(0.0, vinf)
    print(f"beta = 0, v_inf = {vinf}: theta = {th0:.6f}, Rutherford = {2*np.arctan(1/(20*vinf**2)):.6f}")
for h in [2e-3, 1e-3]:
    th, rp = flyby(0.5, 0.1, h=h)
    print(f"beta = 0.5, v_inf = 0.1, step factor {h}: theta = {th:.6f}, pericentre r = {rp:.3f}")
th_na, rp_na = flyby(0.5, 0.1, anomalous=False)
print(f"beta = 0.5, v_inf = 0.1, anomalous velocity switched off (not Hamiltonian; diagnostic): theta = {th_na:.6f}, pericentre r = {rp_na:.3f}")
