N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

INF = 1 << 60
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(N - 1):
    for k in range(K):
        if i - k >= 0:
            dp[i + 1] = min(dp[i + 1], dp[i - k] + abs(H[i - k] - H[i + 1]))
print(dp[N - 1])
