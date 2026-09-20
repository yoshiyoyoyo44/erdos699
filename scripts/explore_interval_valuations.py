"""Exploration only: adaptive exact interval bounds, not a saved certificate."""
import sys
import time
from certify_large_indices import C, LOG2, log_interval, trial_primes


def run(i):
    ps = [p for p in trial_primes(i) if p < i]
    assert i > 4 * len(ps)
    const = (2*i*(i-1)*LOG2[0]
             -2*sum(k*log_interval(k)[1] for k in range(1, i+1))
             +4*i*(i-1)*(log_interval(C-1)[0]-log_interval(C)[1]))
    E = (C*i).bit_length()
    while const+(i-4*len(ps))*(i-1)*E*LOG2[0] <= 0:
        E += 1
    cap = 1 << E
    data = []
    for p in ps:
        q = p
        powers = []
        while q < cap:
            if i % q:
                powers.append((q, i % q))
            q *= p
        data.append((log_interval(p)[1], powers))
    stack = [(C*i, cap-1)]
    tested = leaves = 0
    failed = []
    started = time.monotonic()
    while stack:
        lo, hi = stack.pop()
        upper = 0
        for logp, powers in data:
            e = 0
            for q, r in powers:
                if q > hi:
                    break
                if lo % q < r or hi//q > lo//q:
                    e += 1
            upper += e*logp
        tested += 1
        margin = const+i*(i-1)*log_interval(lo)[0]-4*(i-1)*upper
        if margin > 0:
            leaves += 1
        elif lo == hi:
            failed.append(lo)
        else:
            mid = (lo+hi)//2
            stack.extend([(mid+1, hi), (lo, mid)])
        if tested > 100000:
            return i, E, tested, len(failed), 'limit', round(time.monotonic()-started, 2)
    return i, E, tested, len(failed), failed[:10], round(time.monotonic()-started, 2)


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        print(run(int(arg)), flush=True)
