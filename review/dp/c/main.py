N = int(input())
acts = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = acts[0]

for i in range(N - 1):
    dp[i + 1][2] = max(dp[i][0] + acts[i + 1][2], dp[i][1] + acts[i + 1][2])
    dp[i + 1][0] = max(dp[i][1] + acts[i + 1][0], dp[i][2] + acts[i + 1][0])
    dp[i + 1][1] = max(dp[i][2] + acts[i + 1][1], dp[i][0] + acts[i + 1][1])
print(max(dp[-1]))
