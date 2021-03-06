from functools import reduce
from operator import mul
from collections import Counter
from itertools import accumulate

N = int(input())

A = map(int, input().split())

s = list(accumulate(A, initial=0))
cnt = Counter(s)


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


ans = 0
for k, v in cnt.items():
    if v <= 1:
        continue
    ans += comb(v, 2)
print(ans)
