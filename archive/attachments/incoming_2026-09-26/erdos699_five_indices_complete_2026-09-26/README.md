# Erdos 699: five complete index cases

The proved indices are 95, 99, 103, 107, 119. Each conclusion covers all
integers i < j <= n/2, with no upper bound on n. See REPORT.md for the proof.
This is not a complete solution of Erdos problem 699.

## Reproduce

Python 3, standard library only:

```sh
python3 verify.py
python3 audit_cover.py
```

Expected: PASS for all five indices, 81,957 certified intervals, 888 small
exceptions eliminated, and a full sieve through 2,000,100. The infinite tail
is certified separately by exact integer comparisons and a monotonicity proof.

To regenerate certificates:

```sh
python3 generate.py
python3 generate_small.py
python3 verify.py
python3 audit_cover.py
```

The verifier imports neither generator. Its logarithm enclosure algorithm,
precision, interval intersection expression, and prime sieve differ from those
used by the generators. No probabilistic primality tests are used.

## Dependencies

The new five-index result does not depend on A=100 near-collision certificates,
Matveev, the previous discriminant theorem, or unprovided digit-polynomial
manuscripts. The mathematical prerequisites are proved in REPORT.md from
Legendre's factorial valuation formula and elementary divisibility.

The change in the unresolved count, 113 to 108, additionally uses the previous
repository status at f5a28d1037f35fdccc7a014e958db6fd666d220b.

Independent human peer review and Lean formal verification have not been
performed. No global novelty claim is made. Earlier integrated research is
preserved as previous_research.zip; it is not needed to run this verifier.
