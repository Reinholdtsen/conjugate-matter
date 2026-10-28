"""Viel et al. 2005 WDM transfer-function fit [S via search summaries], shared by sat_proxy.py:
T^2 = [1 + (alpha k)^(2 nu)]^(-10/nu), nu = 1.12,
alpha = 0.049 (m/keV)^-1.11 (Omega_wdm/0.25)^0.11 (h/0.7)^1.22 Mpc/h, Omega_wdm = Omega_c (Planck 2018)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dark-tests"))
import cosmo as C


def T2_wdm(k_mpc, m_keV):
    alpha = 0.049 * m_keV**-1.11 * (C.Oc / 0.25)**0.11 * (C.h / 0.7)**1.22
    nu = 1.12
    return (1 + (alpha * k_mpc / C.h)**(2 * nu))**(-10 / nu)
