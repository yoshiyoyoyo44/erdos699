# Research ledger — 2026-09-26

Target: eliminate at least one of the five unresolved indices
95,99,103,107,119 for every n,j, rather than add only necessary conditions.

## Discovery and correction record

- The initial small-prime cofactor-product approach still faced moving
  coefficients in near-prime-power equations.
- The factor-allocation grid suggested using row, column, and diagonal
  capacities simultaneously. The weighted covering inequality provides a
  bound of approximately Q <= n^(2i/3), improving the exponent needed here.
- An exploratory tail calculation initially inserted h_i=i for all five
  indices. This is invalid for prime indices 103,107. The committed generators,
  verifier, certificates, and report all use h_i=1 for those two indices.
  The tail cutoff remains 10^19 after this correction.
- The final proof uses Q_s from the actual binomial coefficient, simplifying
  the p=i boundary relative to the full-prime-power factors in earlier work.

## Claim registry

1. PROVED: counterexample primes p>=i yield a pairwise coprime triangular
   factor allocation, with row, column and diagonal divisibility.
2. PROVED: nonnegative weights satisfy w_s+x_u+z_(s-u)>=d and all three
   weight sums equal S. Hence 4^S Q^d <= n^(3S).
3. PROVED: the small-prime part of C(n,i) is <=n^pi/h_i; the ratio used for
   the tail is increasing when Delta=d(i-pi)-3S>0.
4. EXHAUSTIVE-COMPUTATION: all five exact tail endpoint inequalities.
5. EXHAUSTIVE-COMPUTATION: all 81,957 interval certificates, with complete
   contiguous coverage from 2,000,000 to the appropriate tail cutoff minus one.
6. EXHAUSTIVE-COMPUTATION: all small n using a complete prime sieve and
   exhaustive residual-j constraints for the 888 exceptions.
7. PROVED + EXHAUSTIVE-COMPUTATION: the original conjecture holds for all
   five target indices and every admissible n,j.
8. OPEN-GAP: no claim in this package that the other 108 indices are solved.

## Hostile audit

Checked the uniqueness of the row of each p>=i; the active p=i exponent;
coprimality of all cells; the sign of j-u and y-u; double counting via exact
weights; non-strict versus strict inequality use; h_i at prime indices;
tail monotonicity; finite coverage endpoints; exact logarithm rounding and
tail errors; primality of every small-range certificate prime; and complete
enumeration of j after the anchor constraint.

The independent verifier uses direct rational-series integer divisions at
128 bits, against the generator's outward interval recurrences at 192 bits.
It does not import the generators. Unconditional cover identities were
additionally checked on 22,035 triples and 20 target-index boundary examples.
This is separate software verification, not independent human peer review.

## Sources and priority

Frontier snapshot: yoshiyoyoyo44/erdos699, commit
f5a28d1037f35fdccc7a014e958db6fd666d220b.
The user's previous integrated report is included as previous_research.zip.
Bergman's original preprint was consulted for the classical Kummer framing.
No claim of worldwide novelty follows from this limited literature check.

## Next question

Determine which additional indices have a positive weighted-cover degree gap
and can be closed by a complete finite verification. The current deliverable
deliberately counts only the five fully checked targets as newly solved.
