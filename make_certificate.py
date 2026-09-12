"""Produce elementary Lucas primality certificates for the saved sieve."""
import json
from math import gcd, prod
from pathlib import Path
from sympy import factorint

cert = {'2': {'factors': [], 'witnesses': []}}


def prove(p):
    key = str(p)
    if key in cert:
        return
    fs = [(int(q), int(e)) for q, e in sorted(factorint(p-1).items())]
    assert prod(q**e for q, e in fs) == p-1
    ws = []
    for q, _ in fs:
        prove(q)
        a = 2
        while not (pow(a, p-1, p) == 1 and gcd(pow(a, (p-1)//q, p)-1, p) == 1):
            a += 1
            if a >= p:
                raise ValueError(('No primality witness', p, q))
        ws.append([q, a])
    cert[key] = {'factors': fs, 'witnesses': ws}


if __name__ == '__main__':
    import sys
    files = sys.argv[1:]
    for file in files:
        data = json.loads(Path(file).read_text(encoding='utf-8'))
        for row in data['certificates']:
            for p, _ in row['Q1_factors']:
                prove(p)
    Path('prime_certificates.json').write_text(json.dumps(cert, indent=2), encoding='utf-8')
    print(f'Produced {len(cert)} recursively checkable prime certificates.')
