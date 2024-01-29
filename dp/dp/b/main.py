N, K = list(map(int, input().split()))
h = [0] + list(map(int, input().split()))

INF = 1 << 60
dp = [INF] * (N + 1)
dp[0] = 0
dp[1] = 0
dp[2] = abs(h[2] - h[1])

for i in range(3, N + 1):
    for k in range(1, K + 1):
        if i - k > 0:
            dp[i] = min(dp[i], dp[i - k] + abs(h[i] - h[i - k]))
print(dp[N])
