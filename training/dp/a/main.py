N = int(input())
H = list(map(int, input().split()))

INF = 1 << 60
dp = [INF] * N
dp[0] = 0
dp[1] = abs(H[0] - H[1])

for i in range(N - 2):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i + 1] - H[i]))
    dp[i + 2] = min(dp[i] + abs(H[i + 2] - H[i]), dp[i + 1] + abs(H[i + 2] - H[i + 1]))
print(dp[N - 1])
