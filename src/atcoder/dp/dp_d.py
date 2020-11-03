N, W = map(int, input().split(" "))
bagages = [list(map(int, input().split(" "))) for _ in range(N)]

dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

for i, (w, v) in enumerate(bagages):
    for j in range(W + 1):
        if j - w >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

print(dp[N][W])
