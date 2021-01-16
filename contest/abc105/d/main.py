from collections import Counter
from functools import reduce
from itertools import accumulate
from operator import mul


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


N, M = map(int, input().split())
A = map(lambda x: int(x) % M, input().split())

counter = Counter(accumulate(A, lambda x, y: (x + y) % M, initial=0))

ans = 0
for k, v in counter.items():
    if v >= 2:
        ans += comb(v, 2)
print(ans)
