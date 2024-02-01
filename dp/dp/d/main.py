N, W = list(map(int, input().split()))

w, v = [0], [0]
for _ in range(N):
    _w, _v = list(map(int, input().split()))
    w.append(_w)
    v.append(_v)


dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, W + 1):
        if j - w[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

print(max(dp[N]))
