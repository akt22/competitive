N, M = map(int, input().split())
distances = [int(input()) for _ in range(N)]
weathers = [int(input()) for _ in range(M)]

INF = 10**9
dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M):
        if dp[i][j] != INF:
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + distances[i] * weathers[j])
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j])

print(min(dp[-1]))
