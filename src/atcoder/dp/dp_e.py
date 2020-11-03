N, W = map(int, input().split(" "))
bagages = [list(map(int, input().split(" "))) for _ in range(N)]

max_v = 100100
INF = 2**31 - 1

dp = [[INF for _ in range(max_v + 1)] for _ in range(N + 1)]

dp[0][0] = 0

for i, (w, v) in enumerate(bagages):
    for j in range(max_v + 1):
        if j - v >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - v] + w)
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

ans = 0
for idx, elem in enumerate(dp[N]):
    if elem <= W:
        ans = idx
print(ans)
