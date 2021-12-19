N, W = list(map(int, input().split()))
w, v = [], []
total_v = 0
for _ in range(N):
    _w, _v = list(map(int, input().split()))
    w.append(_w)
    v.append(_v)
    total_v += _v

INF = 1 << 60
dp = [[INF] * (total_v + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(total_v + 1):
        if j - v[i] >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - v[i]] + w[i])
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
ans = 0
for i, w in enumerate(dp[N]):
    if w <= W:
        ans = i
print(ans)
