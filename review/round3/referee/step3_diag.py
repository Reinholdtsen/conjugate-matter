import sympy as sp
for d in [1,2,3]:
    A = sp.Matrix(d,d,lambda i,j: sp.Symbol(f"a{min(i,j)}{max(i,j)}")); B = sp.Matrix(d,d,lambda i,j: sp.Symbol(f"b{min(i,j)}{max(i,j)}"))
    C = sp.Matrix(d,d,lambda i,j: sp.Symbol(f"c{i}{j}"))
    I = sp.eye(d); Z = sp.zeros(d)
    om = sp.BlockMatrix([[Z,I],[-I,Z]]).as_explicit(); et = sp.BlockMatrix([[Z,I],[I,Z]]).as_explicit()
    H = sp.BlockMatrix([[A,C],[C.T,B]]).as_explicit()
    E1 = sp.expand((et.inv()*H)**2 - sp.eye(2*d)); E2 = sp.expand((om.inv()*H)**2 + sp.eye(2*d))
    s11 = sp.expand(E1[:d,:d] + E2[:d,:d]); d11 = sp.expand(E1[:d,:d] - E2[:d,:d])
    print(f"d={d}: (1,1)-blocks: E1+E2 == 2 (C^T)^2 : {sp.expand(s11 - 2*C.T*C.T)==sp.zeros(d)} ; E1-E2 == 2(BA-1): {sp.expand(d11 - 2*(B*A-I))==sp.zeros(d)}")
