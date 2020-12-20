N = int(input())
h = list(map(int, input().split(" ")))

INF = 10 ** 6
dp = [INF for _ in range(N)]

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i]), dp[i - 2] + abs(h[i - 2] - h[i]))

print(dp[N - 1])
