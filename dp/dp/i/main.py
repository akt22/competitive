N = int(input())
p = list(map(float, input().split()))

dp = [[0.0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1.0

for i in range(N):
    pi = p[i]
    for j in range(N):
        dp[i + 1][j] += dp[i][j] * (1.0 - pi)
        dp[i + 1][j + 1] += dp[i][j] * pi

# Nが奇数なので、表がN ~ (N/2+1)枚出る時が求める確率
print(sum(dp[N][N // 2 + 1 :]))
