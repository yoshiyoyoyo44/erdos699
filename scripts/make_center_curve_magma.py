"""Generate direct center/endpoint curves for fixed w/lambda, without T/u branches."""
from repo_paths import artifact_path
import json
from pathlib import Path

CASES = [(61, 1, 1), (55, 1, 3), (37, 3, 1), (317, 1, 1)]
ENDPOINT_CASES = [(2, 1, 1), (2, 1, 3)]


def source(w, d1, d2):
    return f'''// Direct center curve: w={w}, delta1={d1}, delta2={d2}.
// No conjectural class-group bound is enabled.
SetSeed(699);
w:={w}; d1:={d1}; d2:={d2}; c0:=d1^2*d2;
print "CENTER_CASE",w,d1,d2;
E:=EllipticCurve([0,-10*w*c0,0,8*w^2*c0*(w+2*c0),0]);
assert Discriminant(E) eq 4096*w^6*c0^3*(w+2*c0)^2*(9*c0-8*w);
P:=E![2*w*c0,4*w^2*c0,1];
assert (2*P)[1] eq (2*w+3*c0)^2/4;
G,mp,rank_proved,group_proved:=MordellWeilGroup(E);
print "PROOF_FLAGS",rank_proved,group_proved;
assert rank_proved and group_proved;
basis:=[mp(G.i):i in [1..Ngens(G)] | Order(G.i) eq 0];
print "RANK",#basis;
print "FREE_BASIS",basis;
points:=IntegralPoints(E:FBasis:=basis,SafetyFactor:=2);
print "POINT_COUNT",#points;
for R in points do
    assert R[3] eq 1;
    print "POINT",Integers()!R[1],Integers()!R[2];
end for;
print "CENTER_CASE_COMPLETE",w,d1,d2;
'''


def main():
    rows=[]
    for w,d1,d2 in CASES:
        name=f'i3_center_w{w}_d{d1}{d2}.magma'
        artifact_path(name).write_text(source(w,d1,d2),encoding='utf-8')
        rows.append(dict(w=w,delta1=d1,delta2=d2,input=name,
                         response=f'magma_center_w{w}_d{d1}{d2}.xml',
                         role='required_complete' if w != 317 else 'regression_attempt'))
    artifact_path('center_curve_cases.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
    endpoint_rows=[]
    for lam,d1,d2 in ENDPOINT_CASES:
        name=f'i3_endpoint_l{lam}_d{d1}{d2}.magma'
        artifact_path(name).write_text(endpoint_source(lam,d1,d2),encoding='utf-8')
        endpoint_rows.append(dict(lam=lam,delta1=d1,delta2=d2,input=name,
                                 response=f'magma_endpoint_l{lam}_d{d1}{d2}.xml'))
    artifact_path('endpoint_curve_cases.json').write_text(json.dumps(endpoint_rows,indent=2)+'\n',encoding='utf-8')
    print(f'Generated {len(rows)} center and {len(endpoint_rows)} endpoint curve inputs.')


def endpoint_source(lam,d1,d2):
    return f'''// Direct endpoint curve: lambda={lam}, delta1={d1}, delta2={d2}.
// No conjectural class-group bound is enabled.
SetSeed(699);
lam:={lam}; d1:={d1}; d2:={d2}; c0:=d1^2*d2;
print "ENDPOINT_CASE",lam,d1,d2;
E:=EllipticCurve([0,-16*c0*lam,0,128*c0*lam^3,256*c0^2*lam^4]);
assert Discriminant(E) eq -1048576*c0^3*lam^7*(128*lam^2+107*c0*lam-64*c0^2);
G,mp,rank_proved,group_proved:=MordellWeilGroup(E);
print "PROOF_FLAGS",rank_proved,group_proved;
assert rank_proved and group_proved;
basis:=[mp(G.i):i in [1..Ngens(G)] | Order(G.i) eq 0];
print "RANK",#basis;
print "FREE_BASIS",basis;
points:=IntegralPoints(E:FBasis:=basis,SafetyFactor:=2);
print "POINT_COUNT",#points;
for P in points do
    assert P[3] eq 1;
    print "POINT",Integers()!P[1],Integers()!P[2];
end for;
print "ENDPOINT_CASE_COMPLETE",lam,d1,d2;
'''


if __name__=='__main__':
    main()
