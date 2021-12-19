from collections import defaultdict

import sys
sys.setrecursionlimit(500000)

N, M = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(M):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    g[a].append(b)

dp = [-1] * (N + 1)


def rec(i):
    if dp[i] != -1:
        return dp[i]
    ret = 0
    for dest in g[i]:
        ret = max(ret, rec(dest) + 1)
    dp[i] = ret
    return ret


ans = 0
for i in range(N):
    ans = max(ans, rec(i))
print(ans)
