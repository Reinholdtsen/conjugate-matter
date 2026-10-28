"""Independent check of the static operator's top eigenvalues by a method that uses
no angular decomposition and no Mehler formula: a 3D Cartesian velocity grid, the gate
convolution applied spectrally (FFT with the gate's analytic 3D Fourier transform,
zero-padded box), gravity as the rank-one term, power iteration / subspace iteration.

Operator (sigma = 1, symmetric form):
  (K psi)(v) = p0^(1/2)(v) * Int d^3v' [1 + gt * W(|v-v'|/v*)] p0^(1/2)(v') psi(v')
with p0 the unit Maxwellian. Unstable iff (k/k_J)^2 < top eigenvalue (static criterion).
Anchor independent of the claim: Rasmussen & Williams (GPML, 2006, sec. 4.3.1) closed form
for the eigenvalues of a squared-exponential kernel under a Gaussian measure (dagger: from
memory), and the rank-one gravity eigenvalue = Int p0 = 1.
"""
import numpy as np, sys

L = 7.0
N = 64                       # grid points per axis on [-L, L)
h = 2 * L / N
v1 = -L + h * np.arange(N)
VX, VY, VZ = np.meshgrid(v1, v1, v1, indexing='ij')
V2 = VX**2 + VY**2 + VZ**2
sqp0 = (2 * np.pi) ** (-0.75) * np.exp(-V2 / 4.0)
del VX, VY, V2
NP = 2 * N                   # zero-padded box
kk = 2 * np.pi * np.fft.fftfreq(NP, d=h)
kz_r = 2 * np.pi * np.fft.rfftfreq(NP, d=h)
KX, KY, KZ = np.meshgrid(kk, kk, kz_r, indexing='ij')
K2 = KX**2 + KY**2 + KZ**2
del KX, KY, KZ

def What(gate, vs):
    k = np.sqrt(K2)
    if gate == 'gauss':      # W = exp(-s^2/2)
        return (2 * np.pi * vs**2) ** 1.5 * np.exp(-K2 * vs**2 / 2)
    if gate == 'rat2':       # W = (1 + s^2/2)^-2 ; FT of (1+u^2/a^2)^-2 is pi^2 a^3 exp(-a k)
        a = np.sqrt(2) * vs
        return np.pi**2 * a**3 * np.exp(-a * k)
    raise ValueError

def make_op(gate, r, gt, grav=True):
    vs = 1.0 / r
    Wk = What(gate, vs) if gt != 0 else None
    def op(psi):
        g = sqp0 * psi
        out = np.zeros_like(psi)
        if grav:
            out += g.sum() * h**3
        if gt != 0:
            pad = np.zeros((NP, NP, NP))
            pad[:N, :N, :N] = g
            conv = np.fft.irfftn(np.fft.rfftn(pad) * Wk, s=(NP, NP, NP))[:N, :N, :N]
            out = out + gt * conv
        return sqp0 * out
    return op

def top_eigs(op, parity=None, nvec=3, iters=60, seed=1):
    """Block (subspace) iteration with Rayleigh-Ritz; parity='odd' restricts to v_z-odd."""
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((nvec, N, N, N))
    # build parity projector using the grid symmetry v -> -v about 0 (grid is -L..L-h; index map i -> N-i mod N)
    idx = (-np.arange(N)) % N
    def P(x):
        if parity == 'odd':
            return 0.5 * (x - x[:, :, idx])
        if parity == 'even':
            return 0.5 * (x + x[:, :, idx])
        return x
    for it in range(iters):
        Y = np.array([P(op(P(x))) for x in X])
        # orthonormalize Y (Gram-Schmidt via QR on flattened)
        Q, _ = np.linalg.qr(Y.reshape(nvec, -1).T)
        X = Q.T.reshape(nvec, N, N, N)
    AX = np.array([P(op(P(x))) for x in X]).reshape(nvec, -1)
    H = X.reshape(nvec, -1) @ AX.T
    H = 0.5 * (H + H.T)
    return np.sort(np.linalg.eigvalsh(H))[::-1]

def rw_closed(r):
    a = 0.25; b = r**2 / 2; c = np.sqrt(a * a + 2 * a * b); A = a + b + c
    lam0 = np.sqrt(2 * a / A); q = b / A
    return lam0**3, q

if __name__ == '__main__':
    print(f"grid N={N}^3, L={L}, h={h:.4f}, padded {NP}^3")
    op = make_op('gauss', 1.0, 0.0, grav=True)
    print("gravity only: top eigenvalues", top_eigs(op, nvec=2, iters=3))
    for r in [0.25, 1.2917, 4.0, 8.333]:
        Lg, q = rw_closed(r)
        ope = make_op('gauss', r, 1.0, grav=False)
        ev = top_eigs(ope, parity='even', nvec=2, iters=60 if r < 5 else 120)
        od = top_eigs(ope, parity='odd', nvec=2, iters=60 if r < 5 else 120)
        print(f"gate only r={r}: FFT top even={ev[0]:.7e} (closed Lam_g={Lg:.7e}); "
              f"top odd={od[0]:.7e} (closed Lam_g*q={Lg*q:.7e})")
        sys.stdout.flush()
    cases = [('gauss', 1.2917, 10.0, 2.30503422), ('gauss', 1.2917, 100.0, 15.633172),
             ('gauss', 1.2917, 1.0, 1.113881), ('gauss', 0.25, 1.0, 1.839833),
             ('gauss', 4.0, 1e4, 107.742112), ('gauss', 8.333, 1e4, 14.548549),
             ('gauss', 1.2917, 281.0, 42.64197)]
    for gate, r, gt, claim in cases:
        op = make_op(gate, r, gt, grav=True)
        ev = top_eigs(op, parity='even', nvec=3, iters=80 if r < 5 else 150)
        print(f"{gate} r={r} gt={gt}: FFT top two even = {ev[0]:.7f}, {ev[1]:.6f}   agent's Lambda_0 = {claim}")
        sys.stdout.flush()
    for r in [8.333, 16.0]:
        op = make_op('rat2', r, 1.0, grav=False)
        ev = top_eigs(op, parity='even', nvec=2, iters=150)
        print(f"rat2 gate only r={r}: top = {ev[0]:.6e}, Lam*r^3 = {ev[0]*r**3:.5f} (agent: "
              f"{'1.00471' if r < 10 else '1.22686'}; limit sqrt(pi) = {np.sqrt(np.pi):.5f})")
