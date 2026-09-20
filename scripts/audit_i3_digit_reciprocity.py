"""Exact checks accompanying the general proofs of 2026-09-14.

These finite checks are not a proof of the unbounded Erdos problem. No new
finite exclusion range, external integer-point computation, or other AI is used.
"""
from repo_paths import artifact_path
import json
from math import gcd, isqrt
from pathlib import Path

import sympy as sy


def val(n, p):
    assert n > 0
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def digitsum(n, p):
    total = 0
    while n:
        total += n % p
        n //= p
    return total


def allowed(n, j, p):
    while n or j:
        if j % p > n % p:
            return False
        n //= p
        j //= p
    return True


def binomial_val(n, j, p):
    def fv(k):
        result = 0
        while k:
            k //= p
            result += k
        return result
    return fv(n) - fv(j) - fv(n-j)


def symbolic():
    A, B, C, a, b, T, x, G, H, d1, d2, n = sy.symbols(
        'A B C a b T x G H d1 d2 n')
    delta = d1*d2
    determinant = T*T*x*x*B*C*G*H-A*A*a*b-d1
    factorization = d2*A*B*C+1-n/2
    expressions = [A*(delta*B*C-A*a*b)-d1*n/2+T*T*x*x*B*C*G*H
                   -determinant-d1*factorization]
    eta, zeta, t = sy.symbols('eta zeta t')
    dB = a*zeta+t*b*H
    dC = b*eta+t*a*G
    expressions.append(dB*dC-delta*A*a*b-t*(a*G*dB+b*H*dC)
                       -a*b*(eta*zeta-delta*A-t*t*G*H))
    assert all(sy.expand(z) == 0 for z in expressions)
    return len(expressions)


def digit_checks():
    count = prefixes = 0
    for p in (3, 5, 7, 11):
        for n in range(1, 401):
            for j in range(n+1):
                diff = digitsum(j,p)+digitsum(n-j,p)-digitsum(n,p)
                assert diff == (p-1)*binomial_val(n,j,p)
                ok = allowed(n,j,p)
                assert ok == (diff == 0)
                count += 1
                if not ok:
                    continue
                power = p
                while power <= p*n:
                    d = n % power
                    if d < p:
                        assert j % power <= d
                        assert (n-j) % power == d-j % power
                        prefixes += 1
                    power *= p
    witnesses = []
    n,j = 76672,26775
    for p in (17,41):
        N = (n-2)//p
        J = j//p if p == 17 else (j-2)//p
        row = dict(p=p, N=N, J=J, digit_sums=[digitsum(J,p),digitsum(N-J,p),digitsum(N,p)],
                   binomial_valuation=binomial_val(n,j,p))
        assert row['binomial_valuation'] == (1 if p==17 else 2)
        assert row['binomial_valuation'] == binomial_val(N,J,p)
        witnesses.append(row)
    return dict(additions=count,prefixes=prefixes,relaxed_example=witnesses)


def sparse_and_reciprocity():
    primes = list(map(int,sy.primerange(3,150)))
    checks = reciprocal = 0
    for p in primes:
        for r in range(1,16,2):
            for s in range(1,16,2):
                for a,b in ((0,0),(0,1),(2,0)):
                    X,Y = p**a*(p**r+1),p**b*(p**s+1)
                    assert digitsum(X,p)==digitsum(Y,p)==2
                    assert gcd(X,Y)==p**gcd(r,s)+1
                    assert val(X,2)==val(Y,2)==val(p+1,2)
                    checks += 1
        if p%4 != 3:
            continue
        for ell in primes:
            if ell==p:
                continue
            # Exact existence of an odd exponent, using the finite group order.
            roots = [d for d in range(1,2*ell,2) if pow(p,d,ell)==ell-1]
            if roots:
                assert pow(ell,(p-1)//2,p)==1
                if ell%4==3:
                    assert not any(pow(ell,d,p)==p-1 for d in range(1,2*p,2))
                reciprocal += 1
    # Nonvacuous example of the stronger gcd identity in a carry-free split.
    # This is a split of 2^4, not a candidate for Erdos 699.
    p,X,Y=3,4,12
    assert X+Y==2**4 and allowed(X+Y,X,p)
    assert digitsum(X+Y,p)==4 and val(X,2)==val(Y,2)==2
    assert gcd(X,Y)==p+1==2**2
    return dict(sparse_gcd_checks=checks,reciprocity_implications=reciprocal,
                illustrative_split=dict(p=p,X=X,Y=Y,erdos_candidate=False))


def general_valuation_checks():
    # Check the two unequal-valuation arguments in (9) directly on their RHS.
    # No assertion that these free parameters yield a normalized candidate.
    count = 0
    for gamma,d1,d2 in ((1,1,1),(1,1,3),(1,3,1),(3,1,1)):
        for T in (1,5,7,25,35,49):
            for v in range(1,7):
                for u in (4*v+14,4*v+15):
                    for odd_product in (1,3,5,7,35):
                        rhs=d1*gamma*T*2**(u-1)-T*T*2**(2*v)*odd_product
                        assert rhs>0 and val(rhs,2)==2*v
                        assert gcd(rhs//T,T)==1
                        count += 1
    return count


def weak_family():
    modulus=13**3
    assert pow(2,2028,modulus)==1
    assert all(pow(2,2028//p,modulus)!=1 for p in (2,3,13))
    assert pow(2,614,modulus)==17
    assert pow(2,52,53)==1
    assert all(pow(2,52//p,53)!=1 for p in (2,13))
    assert 2028%52==0
    residues=[]
    for k in range(4):
        u=613+2028*k
        Q=2**(u-1)-1
        assert Q%13==0
        K=Q//13
        assert (4*K-1)%169==0
        b=(4*K-1)//169
        assert b%2 and 4*K-169*b==1
        numerator=K-13*b
        assert numerator>0 and val(numerator,2)==2
        W=numerator//4
        assert gcd(W,13*K)==1 and 13*W+K==2**(u-3)
        D=numerator*numerator-4*b*K
        assert D>0 and isqrt(D)**2!=D
        assert (K%53,b%53,D%53)==(32,18,22)
        residues.append(dict(u=u,K_mod53=32,ab_mod53=18,discriminant_mod53=22))
    assert pow(22,26,53)==52
    return dict(examples=residues,period=2028,obstructing_prime=53,
                nonresidue=22,all_k_excluded_by_split=True,
                family_is_erdos_counterexamples=False)


def main():
    result=dict(status='verified',symbolic_identities=symbolic(),
                digits=digit_checks(),sparse=sparse_and_reciprocity(),
                unequal_valuation_checks=general_valuation_checks(),weak_family=weak_family(),
                pure_power_u179_scan_independently_replayed=False,
                complete_i3_solution=False,complete_erdos699_solution=False)
    artifact_path('verification_i3_digit_reciprocity.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
