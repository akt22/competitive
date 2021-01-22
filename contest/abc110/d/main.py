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


def comb(n, r, mod=None):
    r = min(n - r, r)
    if r == 0:
        return 1
    if mod is None:
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1, r + 1))
        return over // under
    else:
        x, y = 1, 1
        for i in range(1, r + 1):
            x = x * (n + 1 - i) % mod
            y = y * i % mod
        return x * pow(y, mod - 2, mod) % mod


d = prime_factorize(M)


ans = 1
for p, k in d.items():
    each = comb(k + N - 1, N - 1)
    ans = (ans * each) % MOD
print(ans)
