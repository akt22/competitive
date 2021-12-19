from collections import defaultdict
import sys
sys.setrecursionlimit(500000)

N, M = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(M):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    g[a].append(b)

dp = [-1] * N


def rec(v):
    if dp[v] != -1:
        return dp[v]
    ret = 0
    for dest in g[v]:
        ret = max(ret, rec(dest) + 1)
    dp[v] = ret
    return ret


for i in range(N):
    rec(i)
print(max(dp))
