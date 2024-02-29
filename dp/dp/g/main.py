import sys

from collections import defaultdict

sys.setrecursionlimit(500000)

N, M = list(map(int, input().split()))
g = defaultdict(list)

for _ in range(M):
    x, y = list(map(int, input().split()))
    g[x].append(y)

dp = [-1] * (N + 1)


def rec(i):
    if dp[i] != -1:
        return dp[i]
    dp[i] = 0
    for dest in g[i]:
        dp[i] = max(dp[i], rec(dest) + 1)
    return dp[i]


for i in range(1, N + 1):
    rec(i)

print(max(dp))
