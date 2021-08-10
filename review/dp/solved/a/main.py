N = int(input())
h = list(map(int, input().split()))

INF = 1 << 60
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(N - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i + 1] - h[i]))
    if i > 0:
        dp[i + 1] = min(dp[i + 1], dp[i - 1] + abs(h[i + 1] - h[i - 1]))
print(dp[N - 1])
