from collections import defaultdict

import sys

sys.setrecursionlimit(500000)

N, M = list(map(int, input().split()))
g = defaultdict(list)

for _ in range(M):
    x, y = list(map(int, input().split()))
    g[x].append(y)

dp = [-1] * (N + 1)


def rec(dep):
    if dp[dep] != -1:
        return dp[dep]
    ret = 0
    for dest in g[dep]:
        ret = max(ret, rec(dest) + 1)
    dp[dep] = ret
    return ret


for i in range(1, N + 1):
    rec(i)
print(max(dp))
