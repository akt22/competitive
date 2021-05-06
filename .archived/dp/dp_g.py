import sys

from collections import defaultdict
from functools import lru_cache

sys.setrecursionlimit(10**6)

N, M = map(int, input().split(" "))

G = defaultdict(list)
dp = [-1 for _ in range(N + 1)]


@lru_cache(maxsize=None)
def rec(v: int) -> int:
    if dp[v] != -1:
        return dp[v]

    res = 0
    for nv in G[v]:
        res = max(res, rec(nv) + 1)
    dp[v] = res
    return res


for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split(" "))
    G[x].append(y)

ans = 0
for v in range(N):
    ans = max(ans, rec(v))
print(ans)
