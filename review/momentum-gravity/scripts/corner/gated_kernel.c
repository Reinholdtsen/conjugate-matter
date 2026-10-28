/* Direct-summation pair kernel for the corner model (round 3, label "corner").

   Pair energy (Plummer softening b, both channels softened the same way):
       U_ij = -G m^2 [1 + eps W(s_ij)] / rt_ij,  rt = sqrt(|x_i-x_j|^2 + b^2),
       W(s) = exp(-s^2/2),  s = |w_i - w_j| / v*.
   Reading H ("Hamiltonian", canonical-momentum gate; w = p/m is the canonical momentum per mass):
       xdot_i = w_i + (eps G m / v*^2) sum_j W_ij (w_i - w_j) / rt_ij        (= dH/dp_i)
       wdot_i = -G m sum_j [1 + eps W_ij] (x_i - x_j) / rt_ij^3              (= -dH/dx_i / m)
   Reading F ("force law at fixed velocity", no Hamiltonian): xdot_i = w_i (w is the velocity),
       wdot_i as above.
   phi_i = -G m sum_j [1 + eps W_ij] / rt_ij  (per-unit-mass pair energy of particle i).
   Arrays are row-major n x 3. O(n^2/2) loop over pairs i<j; no heap allocation. */
#include <math.h>

void deriv(int n, const double *x, const double *w, double Gm, double eps,
           double vs2inv, double b2, int hamiltonian,
           double *xdot, double *wdot, double *phi)
{
    int i, j;
    for (i = 0; i < 3 * n; i++) { xdot[i] = 0.0; wdot[i] = 0.0; }
    for (i = 0; i < n; i++) phi[i] = 0.0;
    for (i = 0; i < n; i++) {
        const double xi0 = x[3*i], xi1 = x[3*i+1], xi2 = x[3*i+2];
        const double wi0 = w[3*i], wi1 = w[3*i+1], wi2 = w[3*i+2];
        double ax = 0, ay = 0, az = 0, vx = 0, vy = 0, vz = 0, ph = 0;
        for (j = i + 1; j < n; j++) {
            const double dx = xi0 - x[3*j], dy = xi1 - x[3*j+1], dz = xi2 - x[3*j+2];
            const double du = wi0 - w[3*j], dv = wi1 - w[3*j+1], dw = wi2 - w[3*j+2];
            const double r2 = dx*dx + dy*dy + dz*dz + b2;
            const double rinv = 1.0 / sqrt(r2);
            const double rinv3 = rinv * rinv * rinv;
            const double s2 = (du*du + dv*dv + dw*dw) * vs2inv;
            const double W = (eps != 0.0) ? exp(-0.5 * s2) : 0.0;
            const double fac = Gm * (1.0 + eps * W) * rinv3;
            ax -= fac * dx; ay -= fac * dy; az -= fac * dz;
            wdot[3*j] += fac * dx; wdot[3*j+1] += fac * dy; wdot[3*j+2] += fac * dz;
            const double pe = Gm * (1.0 + eps * W) * rinv;
            ph -= pe; phi[j] -= pe;
            if (hamiltonian && eps != 0.0) {
                const double an = eps * Gm * vs2inv * W * rinv;
                vx += an * du; vy += an * dv; vz += an * dw;
                xdot[3*j] -= an * du; xdot[3*j+1] -= an * dv; xdot[3*j+2] -= an * dw;
            }
        }
        wdot[3*i] += ax; wdot[3*i+1] += ay; wdot[3*i+2] += az;
        xdot[3*i] += vx; xdot[3*i+1] += vy; xdot[3*i+2] += vz;
        phi[i] += ph;
    }
    for (i = 0; i < 3 * n; i++) xdot[i] += w[i];
}
