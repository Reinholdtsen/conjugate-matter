"""d=2: algebraic proof via Groebner basis. Ideal I = <entries of (eta^-1H)^2-1, (omega^-1H)^2+1, t*det(A)-1>.
Check that every c_i and every entry of B*A-1 lies in I (normal form 0)."""
import sympy as sp
d = 2
a0,a1,a2,b0,b1,b2,c0,c1,c2,c3,t = sp.symbols('a0 a1 a2 b0 b1 b2 c0 c1 c2 c3 t')
A = sp.Matrix([[a0,a1],[a1,a2]]); B = sp.Matrix([[b0,b1],[b1,b2]]); C = sp.Matrix([[c0,c1],[c2,c3]])
I2 = sp.eye(2); Z = sp.zeros(2)
om = sp.BlockMatrix([[Z,I2],[-I2,Z]]).as_explicit(); et = sp.BlockMatrix([[Z,I2],[I2,Z]]).as_explicit()
H = sp.BlockMatrix([[A,C],[C.T,B]]).as_explicit()
E = list(sp.expand((et.inv()*H)**2 - sp.eye(4))) + list(sp.expand((om.inv()*H)**2 + sp.eye(4)))
E = [e for e in set(E) if e != 0] + [t*A.det() - 1]
gens = [c0,c1,c2,c3,t,b0,b1,b2,a0,a1,a2]
G = sp.groebner(E, *gens, order='grevlex')
for c in [c0,c1,c2,c3]:
    print(f"normal form of {c} mod I: {G.reduce(c)[1]}")
for e in list(sp.expand(B*A - I2)):
    print(f"normal form of (BA-1) entry {e}: {G.reduce(e)[1]}")
# a non-invertible-A solution with C != 0? search the ideal without the t-equation for a point
E0 = [e for e in set(list(sp.expand((et.inv()*H)**2 - sp.eye(4))) + list(sp.expand((om.inv()*H)**2 + sp.eye(4)))) if e != 0]
G0 = sp.groebner(E0, c0,c1,c2,c3,b0,b1,b2,a0,a1,a2, order='grevlex')
print("Without invertibility: is c0 in the ideal?", G0.reduce(c0)[1] == 0, "| is c0^k for small k?", [G0.reduce(c0**k)[1]==0 for k in (2,3,4)])
print("Is 1 in the ideal without invertibility (i.e. no solutions at all with singular... )?", G0.reduce(sp.Integer(1))[1] == 0)
