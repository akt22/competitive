N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

INF = 1 << 60
dp = [INF] * N

dp[0] = 0
for i in range(N):
    for k in range(1, K + 1):
        if i + k >= N:
            continue
        dp[i + k] = min(dp[i + k], dp[i] + abs(H[i] - H[i + k]))
print(dp[-1])
