N, W = list(map(int, input().split()))
wv = []
total_v = 0
for _ in range(N):
    w, v = list(map(int, input().split()))
    wv.append((w, v))
    total_v += v


INF = 1 << 60
dp = [[INF] * (total_v + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i, (w, v) in enumerate(wv):
    for j in range(total_v + 1):
        if j - v >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - v] + w)
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

ans = 0
for i, w in enumerate(dp[N]):
    if w <= W:
        ans = max(ans, i)
print(ans)
