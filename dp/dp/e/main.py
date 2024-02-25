N, W = list(map(int, input().split()))
w, v = [0], [0]
total_v = 0

for _ in range(N):
    _w, _v = list(map(int, input().split()))
    w.append(_w)
    v.append(_v)
    total_v += _v

INF = 1 << 60
dp = [[INF] * (total_v + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(total_v + 1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        if j - v[i] >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - v[i]] + w[i])

ans = 0
for idx, value in enumerate(dp[N]):
    if value > W:
        continue
    ans = idx

print(ans)
