N, W = list(map(int, input().split()))
w, v = [0], [0]

for _ in range(N):
    _w, _v = list(map(int, input().split()))
    w.append(_w)
    v.append(_v)

sum_v = sum(v)

INF = 1 << 60
dp = [[INF] * (sum_v + 1) for _ in range(N + 1)]
dp[0][0] = 0
dp[1][v[1]] = w[1]

for i in range(1, N + 1):
    for j in range(sum_v + 1):
        if j - v[i] >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - v[i]] + w[i], dp[i - 1][j])
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])

ans = 0
for i, e in enumerate(dp[N]):
    if e <= W:
        ans = max(ans, i)
print(ans)
