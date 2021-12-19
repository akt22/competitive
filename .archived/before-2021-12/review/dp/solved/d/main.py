N, W = list(map(int, input().split()))
bagages = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        if j - bagages[i][0] >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - bagages[i][0]] + bagages[i][1])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
print(dp[N][W])
