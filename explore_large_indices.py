"""Exploratory floating-point screening only, not a certificate."""
from math import log, floor, ceil
import heapq

C = 16598
primes = [p for p in range(2, 900) if all(p%d for d in range(2, int(p**.5)+1))]
bad = []
for i in range(121, 900):
    ps = [p for p in primes if p<i]
    r = len(ps)
    alpha = i/4-r
    assert alpha>0
    log_const = i/2*log(2)-sum(k*log(k) for k in range(1,i+1))/(2*(i-1)) + i*log(1-1/C)
    E = max((C*i).bit_length(), ceil(-log_const/(alpha*log(2)))+1)
    cap = 1<<E
    n0 = C*i
    queue = []
    logU = 0.0
    for p in ps:
        power = p
        e = 1
        while power*p <= n0:
            power *= p
            e += 1
        logU += e*log(p)
        heapq.heappush(queue,(power*p,p,e+1))
    points = 1
    minmargin = log_const+i/4*log(n0)-logU
    lastbad = n0 if minmargin<=0 else None
    while queue and queue[0][0] <= cap:
        n,p,e = heapq.heappop(queue)
        logU += log(p)
        margin = log_const+i/4*log(n)-logU
        minmargin = min(minmargin,margin)
        if margin <= 0:
            lastbad = n
        heapq.heappush(queue,(n*p,p,e+1))
        points += 1
    if lastbad is not None:
        bad.append(i)
    if i%25 == 0 or i in (121,899):
        print(i,'E',E,'points',points,'min',minmargin,'lastbad',lastbad,flush=True)
print('last bad index:', max(bad) if bad else None)
