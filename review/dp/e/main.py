N, W = list(map(int, input().split()))
bagages = [list(map(int, input().split())) for _ in range(N)]

total_v = sum(e for _, e in bagages)

INF = 1 << 60
dp = [[INF] * (total_v + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i, (w, v) in enumerate(bagages):
    for j in range(total_v + 1):
        if j - v >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - v] + w)
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
ans = 0
for j in range(total_v):
    if dp[N][j] <= W:
        ans = j
print(ans)
