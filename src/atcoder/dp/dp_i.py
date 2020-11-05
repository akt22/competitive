N = int(input())
p = list(map(float, input().split(" ")))

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

dp[0][0] = 1.0

for i in range(N):
    for j in range(i + 1):
        dp[i + 1][j] += dp[i][j] * (1.0 - p[i])
        dp[i + 1][j + 1] += dp[i][j] * p[i]

idx = int(N / 2) + 1
print(sum(dp[N][idx:]))
