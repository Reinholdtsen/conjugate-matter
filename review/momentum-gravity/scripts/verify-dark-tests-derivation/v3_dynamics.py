"""
v3_dynamics.py -- are the three readings of U = -Gt m^2 W(|v-v'|/v*)/r consistent
dynamics?  Two-body relative motion (reduced mass mu = m/2), units Gt m = 1, v* = 1,
m = 1, Gaussian W(u) = exp(-u^2/2).
  (iii) force law: mu rdd = -grad_r U at fixed v.  Candidate energies: E_iii = mu v^2/2 + U,
        E_L = mu v^2/2 + U - v.dU/dv (the Lagrangian's energy).
  (ii)  Lagrangian L = mu v^2/2 - U(r, v): EL eqs solved for rdd; E_L conserved.
  (i)   Hamiltonian H = p^2/(2 mu) + U(r, p/mu): Hamilton's eqs; H conserved.
Also: divergence of the (x, v) flow for (iii) (Liouville), and the lone-particle
peculiar-velocity law in a uniform Hubble-flow medium (local limit): (iii) u ~ a^(-1+kappa),
(i) w ~ 1/a and u = (1+kappa) w.
"""
import numpy as np

mu = 0.5
def W(u): return np.exp(-u**2/2)
def dW(u): return -u*np.exp(-u**2/2)
def d2W(u): return (u**2-1)*np.exp(-u**2/2)

def U(r, v):
    return -W(np.linalg.norm(v))/np.linalg.norm(r)      # Gt m^2 = 1
def gradr_U(r, v):
    R = np.linalg.norm(r); return W(np.linalg.norm(v))*r/R**3
def gradv_U(r, v):
    R = np.linalg.norm(r); V = np.linalg.norm(v)
    return -dW(V)*v/V/R if V > 0 else np.zeros(2)
def hessv_U(r, v):
    R = np.linalg.norm(r); V = np.linalg.norm(v); n = v/V
    # d2/dv2 [-W(|v|)]/R = -(W'' n n + W'/V (1 - n n))/R
    return -(d2W(V)*np.outer(n, n) + dW(V)/V*(np.eye(2) - np.outer(n, n)))/R
def mixed_U(r, v):
    # d/dr_j of dU/dv_i = dW(V) n_i r_j /(V-hat...) : dU/dv_i = -W' n_i / R ; d/dr_j (1/R) = -r_j/R^3
    R = np.linalg.norm(r); V = np.linalg.norm(v); n = v/V
    return dW(V)*np.outer(n, r)/R**3

def acc_iii(r, v): return -gradr_U(r, v)/mu
def acc_ii(r, v):
    # d/dt(mu v - dU/dv) = -dU/dr  ->  (mu I - Hv) a = -dU/dr + (mixed) . v
    M = mu*np.eye(2) - hessv_U(r, v)
    rhs = -gradr_U(r, v) + mixed_U(r, v) @ v
    return np.linalg.solve(M, rhs)

def rk4(f, y, dt):
    k1 = f(y); k2 = f(y + dt/2*k1); k3 = f(y + dt/2*k2); k4 = f(y + dt*k3)
    return y + dt/6*(k1 + 2*k2 + 2*k3 + k4)

def run(reading, r0, v0, T=40.0, dt=1e-3):
    if reading in ('iii', 'ii'):
        acc = acc_iii if reading == 'iii' else acc_ii
        f = lambda y: np.concatenate([y[2:], acc(y[:2], y[2:])])
        y = np.concatenate([r0, v0])
    else:   # Hamiltonian in (r, p); gate on p/mu
        def f(y):
            r, p = y[:2], y[2:]; v = p/mu
            rdot = p/mu + gradv_U(r, v)/mu
            pdot = -gradr_U(r, v)
            return np.concatenate([rdot, pdot])
        y = np.concatenate([r0, mu*v0])
    out = []
    n = int(T/dt)
    for i in range(n):
        y = rk4(f, y, dt)
        if i % 200 == 0: out.append(y.copy())
    return np.array(out)

for (r0, v0, lab) in ((np.array([1.0, 0.0]), np.array([0.0, 1.0]), 'strong coupling Gt m/(r v*^2) = 1 at start'),
                     (np.array([4.0, 0.0]), np.array([0.0, 0.45]), 'weak coupling Gt m/(r v*^2) = 0.25 at start')):
  print('---', lab)
  Rmin = None
  for rd in ('iii', 'ii', 'i'):
    tr = run(rd, r0, v0, T=200.0 if r0[0] > 2 else 40.0)
    # minimum over the orbit of the smallest eigenvalue of the Lagrangian kinetic matrix mu I - Hess_v U
    if rd == 'ii':
        ev = [np.linalg.eigvalsh(mu*np.eye(2) - hessv_U(y[:2], y[2:])).min() for y in tr]
        print(f"     (ii) min eigenvalue of mu I - d2U/dv2 along the orbit = {min(ev):+.4f}")
    if rd == 'i':
        Hs = [ (y[2:]@y[2:])/(2*mu) + U(y[:2], y[2:]/mu) for y in tr ]
        print(f"(i)  Hamiltonian: H min/max over orbit = {min(Hs):+.8f} / {max(Hs):+.8f}")
    else:
        Eiii = [mu*(y[2:]@y[2:])/2 + U(y[:2], y[2:]) for y in tr]
        EL = [mu*(y[2:]@y[2:])/2 + U(y[:2], y[2:]) - y[2:]@gradv_U(y[:2], y[2:]) for y in tr]
        Lz = [y[0]*y[3] - y[1]*y[2] for y in tr]
        print(f"({rd}) T+U min/max = {min(Eiii):+.6f} / {max(Eiii):+.6f} ; E_L min/max = {min(EL):+.6f} / {max(EL):+.6f}"
              f" ; L_z min/max = {min(Lz):+.6f} / {max(Lz):+.6f}")

# time reversibility of (iii): integrate forward T, flip v, integrate T: return to start?
f = lambda y: np.concatenate([y[2:], acc_iii(y[:2], y[2:])])
y = np.concatenate([r0, v0])
for i in range(20000): y = rk4(f, y, 1e-3)
y[2:] *= -1
for i in range(20000): y = rk4(f, y, 1e-3)
print(f"(iii) reversibility: after forward 20 + backward 20, |r - r0| = {np.linalg.norm(y[:2]-r0):.2e}")

# Liouville: divergence of the (r, v) flow for (iii) is div_v a = -(1/mu) tr(d grad_r U / dv)
r = np.array([1.0, 0.3]); v = np.array([0.4, 0.9])
h = 1e-6
div = sum((acc_iii(r, v + h*e)[i] - acc_iii(r, v - h*e)[i])/(2*h) for i, e in enumerate(np.eye(2)))
R = np.linalg.norm(r); V = np.linalg.norm(v)
print(f"(iii) div_v(a) at a sample point = {div:+.6f} ; analytic -(1/mu) W'(|v|) (rhat.vhat)/R^2 = {-(1/mu)*dW(V)*(r@v)/(R*V)/R**2:+.6f}")

# lone particle in a uniform Hubble-flow medium (local limit), EdS-free test with constant kappa
kap = 0.2
N = np.linspace(0, 3, 30001); dN = N[1]-N[0]
u_iii = 1.0; w_i = 1.0
for i in range(len(N)-1):
    u_iii += dN*(-1 + kap)*u_iii      # du/dN = -u + kappa u  (anti-drag)
    w_i += dN*(-1.0)*w_i              # dw/dN = -w ; u = (1+kappa) w
print(f"lone particle, kappa={kap}, after ln a = 3: (iii) u/u0 = {u_iii:.5f} (a^(-1+kappa) = {np.exp(3*(-1+kap)):.5f});"
      f" (i) u/u0 = w/w0 = {w_i:.5f} (1/a = {np.exp(-3):.5f})")
