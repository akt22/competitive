from operator import mul
from functools import reduce

W, H = map(int, input().split())

M = 10**9 + 7


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


print(comb(H + W - 2, H - 1, mod=M))
