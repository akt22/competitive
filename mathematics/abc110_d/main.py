from operator import mul
from functools import reduce

N, M = map(int, input().split())
MOD = 10**9 + 7


def prime_factorize(n):
    d = {}
    i = 1
    while i**2 <= n:
        i += 1
        if n % i != 0:
            continue
        d[i] = 0
        while n % i == 0:
            d[i] += 1
            n //= i
    if n != 1:
        d[n] = 1
    return d


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


d = prime_factorize(M)
ans = 1
for k, v in d.items():
    tmp = combinations_count(N + v - 1, v)
    ans = (ans * tmp) % MOD
print(ans)
