from operator import mul
from functools import reduce


n, r = list(map(int, input().split()))


def comb(n, r, mod=None, repetition=False):
    if repetition:
        n = n + r - 1
        r = r - 1
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


MOD = 10**9 + 7

print(comb(n, r, MOD))
