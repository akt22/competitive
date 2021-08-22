N = int(input())
P = list(map(float, input().split()))

dp = [[.0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1. - P[0]
dp[0][1] = P[0]

for i in range(N - 1):
    for j in range(i + 2):
        dp[i + 1][j + 1] += dp[i][j] * P[i + 1]
        dp[i + 1][j] += dp[i][j] * (1. - P[i + 1])

print(sum(dp[N - 1][N // 2 + 1:]))
