#!/usr/bin/env python3
"""
battery.py — the machine-verification battery from HANDOFF.md Appendix A.

Seven tests (T1–T7) of the program's Tier-1 algebra. Every verdict is a
boolean or a number against a tolerance, never a judgement.

    .venv/bin/python verify/battery.py

Exit code 1 if any check fails.

The computations, seeds and RNG call order are Appendix A's, unchanged, so
the printed figures are the ones quoted in papers/broken-born-checkpoint-v2.md
§2 (66.58 vs 63.72; rms 3.29). Those quoted figures are checked as well
("parity"): a parity failure means this environment no longer reproduces
the numbers the papers cite.
"""
import sys
import numpy as np
from math import comb
from itertools import combinations

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)

np.random.seed(0)
d=4
Id=np.eye(d); Zr=np.zeros((d,d))
def randsym(s=1.0):
    m=np.random.randn(d,d)*s; return (m+m.T)/2
def posdef():
    a=np.random.randn(d,d); return a@a.T + d*np.eye(d)
omega=np.block([[Zr,Id],[-Id,Zr]])
eta=np.block([[Zr,Id],[Id,Zr]])
blk=lambda M,i,j: M[i*d:(i+1)*d, j*d:(j+1)*d]

# T1: compatibility theorem
g=posdef()
H=np.block([[g,Zr],[Zr,np.linalg.inv(g)]])
J=np.linalg.inv(eta)@H; Ic=np.linalg.inv(omega)@H
check("T1a diag(g,g^-1) satisfies (eta^-1 H)^2=1 and (omega^-1 H)^2=-1",
      np.allclose(J@J,np.eye(2*d)) and np.allclose(Ic@Ic,-np.eye(2*d)))
A=posdef(); B=posdef(); C=np.random.randn(d,d)*0.3
H2=np.block([[A,C],[C.T,B]])
J2=np.linalg.inv(eta)@H2; I2=np.linalg.inv(omega)@H2
check("T1b generic H violates at least one condition",
      (not np.allclose(J2@J2,np.eye(2*d))) or (not np.allclose(I2@I2,-np.eye(2*d))))
check("T1c proof block (J^2)_21 = A C^T + C A", np.allclose(blk(J2@J2,1,0), A@C.T + C@A))
check("T1c proof block (I^2)_21 = C A - A C^T", np.allclose(blk(I2@I2,1,0), C@A - A@C.T))

# T2: Siegel parametrization
X=randsym(); Y=posdef(); Yi=np.linalg.inv(Y)
HZ=np.block([[Y+X@Yi@X, X@Yi],[Yi@X, Yi]])
IZ=np.linalg.inv(omega)@HZ
check("T2 I[Z]^2 = -1", np.allclose(IZ@IZ,-np.eye(2*d)))
check("T2 H_Z symmetric", np.allclose(HZ,HZ.T))
check("T2 det H_Z = 1", np.isclose(np.linalg.det(HZ),1.0), f"det={np.linalg.det(HZ):.12f}")
check("T2 H_Z positive definite", np.all(np.linalg.eigvalsh(HZ)>0))

# T3: anticommutator blocks {J0,I[Z]} = [[S,A],[A,S]]
M=eta@IZ+IZ@eta
S=Y+X@Yi@X-Yi; Ac=X@Yi-Yi@X
check("T3 {J0,I[Z]} = [[S,A],[A,S]]",
      all([np.allclose(blk(M,0,0),S), np.allclose(blk(M,0,1),Ac),
           np.allclose(blk(M,1,0),Ac), np.allclose(blk(M,1,1),S)]))

# T4: linearized potential is non-Fierz-Pauli
h=randsym(); x=randsym()
tr4=4*np.trace(h@h); fp=4*(np.trace(h@h)-np.trace(h)**2)
for eps in [1e-4, 1e-5]:
    Ye=Id+eps*h; Xe=eps*x; Yei=np.linalg.inv(Ye)
    Se=Ye+Xe@Yei@Xe-Yei
    val=np.trace(Se@Se)/eps**2
    print(f"      T4 eps={eps}: {val:.4f} vs 4Tr(h^2)={tr4:.4f} vs FP={fp:.4f}")
check("T4 Tr(S^2)/eps^2 -> 4Tr(h^2) (rel 1e-5 at eps=1e-5)", abs(val-tr4) <= 1e-5*abs(tr4))
check("T4 limit differs from Fierz-Pauli form (rel > 1%)", abs(val-fp) > 1e-2*abs(fp))
check("T4 parity: 66.58 vs 63.72 as quoted", round(tr4,2)==66.58 and round(fp,2)==63.72,
      f"{tr4:.2f} vs {fp:.2f}")

# T5: palindrome V(1)=2T, exact integers
V1=[comb(4,0)+comb(4,4), comb(4,1)+comb(4,3), comb(4,2)]
T =[comb(3,3),           comb(3,0)+comb(3,2), comb(3,1)]
check("T5 V(1) - 2T = [0,0,0]", [V1[i]-2*T[i] for i in range(3)]==[0,0,0], f"V1={V1} T={T}")

# T6: e_n linearization coefficients
delta=randsym(1e-6)
lam=np.linalg.eigvalsh(Id+delta)
def en(vals,n): return sum(np.prod(c) for c in combinations(vals,n)) if n>0 else 1.0
tr=np.trace(delta)
coef6=[float((en(lam,n)-comb(4,n))/tr) for n in range(5)]
check("T6 e_n(1+delta) linear coefficients = C(3,n-1) = [0,1,3,3,1]",
      np.allclose(coef6,[0,1,3,3,1],atol=1e-3), str([round(c,4) for c in coef6]))

# T7: p4 outside linear span of e_n
rng=np.random.default_rng(1)
E=[];P=[]
for _ in range(300):
    s=rng.uniform(0.5,2.0,size=4)
    E.append([en(s,n) for n in range(5)]); P.append(np.sum(s**4))
E=np.array(E);P=np.array(P)
coef,res,rank,_=np.linalg.lstsq(E,P,rcond=None)
rms=np.sqrt(res[0]/len(P)) if len(res) else np.linalg.norm(E@coef-P)/np.sqrt(len(P))
check("T7 p4 outside span of e_n (rms residual nonzero)", rms > 1e-6, f"rms={rms:.4f}")
check("T7 parity: rms 3.29 as quoted", round(rms,2)==3.29, f"rms={rms:.4f}")

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — all battery checks pass (numpy " + np.__version__ + ").")
