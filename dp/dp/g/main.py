from collections import defaultdict

N, M = list(map(int, input().split()))
g = defaultdict(list)

for _ in range(M):
    x, y = list(map(int, input().split()))
    g[x].append(y)

dp = [0] * (N + 1)
dp[1] = 0

for i in range(2, N + 1):
    for j in g[i]:
        dp[i][j] = max(dp[i][j], dp[i][i] + 1)
