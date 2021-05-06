N = int(input())
activities = [list(map(int, input().split(" "))) for _ in range(N)]

dp = [[0 for _ in range(3)] for _ in range(N + 1)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + activities[i][k])

print(max(dp[N]))
