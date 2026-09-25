# Research ledger — 2026-09-26 JST

Goal: extend the all-index Erdos 699 constraints, integrate the prior index work,
and retain complete proofs and reproducible exact checks.

Frozen source: yoshiyoyoyo44/erdos699 at
f5a28d1037f35fdccc7a014e958db6fd666d220b.
Prior package: erdos699_integrated_power_cofactor_and_digit_bridge_2026-09-25.
No claim of a new global literature priority or of a full solution.

1. PROVED: active full prime-power row factors R_s partition into pairwise
   coprime blocks B_s,u under the counterexample hypothesis. The prime p=i
   correction is restored only if p actually divides C(n,i).
2. PROVED unconditionally: B_s,u B_r,v divides the determinant of the two
   triangular-grid points and (n,j), and |D| <= (i-1)(n-i+1).
3. PROVED using the inherited independent denominator certificate: n>=10^87
   excludes D=0 for distinct positions, yielding the pair-product bound.
4. REFUTED unguarded variant: n=535,i=10,j=214 gives blocks 107 and 53 at
   (0,0),(5,2), D=0, product 5671>4734. Removing D!=0/threshold is invalid.
5. PROVED: at most one block exceeds sqrt((i-1)(n-i+1)). Regular rows above
   this size occupy at least two cells, with at most one exception.
6. PROVED + finite constants: at n>=10^105 every counterexample with
   3<=i<=119 has at least 2(i-pi(i-1))-1 distinct primes >=i in C(n,i).
7. PROVED: source row s>pi(i-1) lies outside a shorter regular prefix once
   denominator b>=i; the gcd exponent improves from (pi+1)/(pi+2) to
   pi/(pi+1). Uniform exponent 30/31 at n>=10^87.
8. PROVED: for row0 the exceptional sets overlap once b>epsilon L_pi.
   Previous power bound guarantees this at n>=10^550; same exponent gain.
9. Failed estimate, not a general impossibility theorem: naive multiplication
   of all row polynomials yields degree >=61 for pi=30 in the optimistic
   no-resonance version, worse than the old degree32. Switched to determinants.
10. OPEN-GAP: no proof of improved exponent for all low rows 1..pi. No proof
    that a favorable digit-polynomial transfer base always exists.

Audit: coprimality, prime=i edge cases, zero determinants, triangular geometry,
strict inequalities, and counterexample-vs-necessary-condition distinctions
were checked separately. verify.py uses direct factorization of small row
integers to cross-check the factorization-free large-integer implementation.
No tests of known counterexamples exist; universal algebraic identities are
tested on all triples in the recorded finite domain instead.

Inherited unverified inputs: the three manuscript bodies named in the user's
index were not available in the prior stage. Their conditional status is
preserved. None of this stage's new theorems depends on them.
