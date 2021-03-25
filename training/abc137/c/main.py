from functools import reduce
from operator import mul
from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(int)

for s in S:
    s = sorted(s)
    d[''.join(s)] += 1


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
for v in d.values():
    if v >= 2:
        ans += comb(v, 2)
print(ans)
