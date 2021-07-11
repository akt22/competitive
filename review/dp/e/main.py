N, W = list(map(int, input().split()))
bagages = [list(map(int, input().split())) for _ in range(N)]

sum_v = sum(v for _, v in bagages)

INF = 1 << 60
dp = [[INF] * (sum_v + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i, (w, v) in enumerate(bagages):
    for j in range(sum_v + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if j - v >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - v] + w)
ans = 0
for v, w in enumerate(dp[N]):
    if w <= W:
        ans = v
print(ans)
