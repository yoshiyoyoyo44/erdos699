"""Complete integral points for the fixed-gap handoff's five small curves."""
from repo_paths import artifact_path
import json
from pathlib import Path


def source(a4):
    return f'''// Fixed-gap auxiliary curve y^2=x^3+{a4}*x.
// Full group proof flags are required; no GRH setting is used.
SetSeed(699);
a4:={a4};
print "GAP_CURVE",a4;
E:=EllipticCurve([0,0,0,a4,0]);
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
print "GAP_CURVE_COMPLETE",a4;
'''


def main():
    rows=[]
    for a4 in [99,399,943,1023,799]:
        name=f'i3_gap_curve_a{a4}.magma'
        artifact_path(name).write_text(source(a4),encoding='utf-8')
        rows.append({'a4':a4,'input':name,'response':f'magma_gap_curve_a{a4}.xml'})
    artifact_path('gap_curve_cases.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    main()
