from functools import reduce
from operator import mul

S = int(input())


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


ans = 0
MOD = 10**9 + 7

for i in range(S // 3):
    idx = i + 1
    r = S - (3 * idx)
    ans += comb(r, idx, mod=MOD, repetition=True)
print(ans % MOD)
