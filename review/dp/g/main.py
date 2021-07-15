from collections import defaultdict

import sys
sys.setrecursionlimit(500000)

N, M = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(M):
    x, y = list(map(int, input().split()))
    x, y = x - 1, y - 1
    g[x].append(y)

dp = [-1] * (N + 1)


def rec(v):
    if dp[v] != -1:
        return dp[v]

    res = 0
    for dest in g[v]:
        res = max(res, rec(dest) + 1)

    dp[v] = res
    return dp[v]


ans = 0
for i in range(N):
    ans = max(ans, rec(i))
print(ans)
