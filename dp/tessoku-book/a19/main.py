N, W = list(map(int, input().split()))
items = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, W + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j])

        w, v = items[i]
        if j - w >= 0:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i][j])  # dp[i][j] は何度も通るので、maxで毎回比較

print(max(dp[N]))
