N, K = map(int, input().split())
orders = {}
for _ in range(K):
    a, b = map(int, input().split())
    b = b - 1
    orders[a] = b

mod = 10000

dp = [[[0] * 3 for _ in range(3)] for _ in range(N + 1)]

if 1 in orders:
    dp[1][orders[1]][1] = 1
else:
    dp[1][0][1] = 1
    dp[1][1][1] = 1
    dp[1][2][1] = 1

for i in range(2, N + 1):
    if i in orders:
        for k in range(3):
            if orders[i] != k:
                dp[i][orders[i]][1] += sum(dp[i - 1][k])
        dp[i][orders[i]][2] = dp[i - 1][orders[i]][1]
    else:
        for j in range(3):
            for k in range(3):
                if j != k:
                    dp[i][j][1] += sum(dp[i - 1][k])
            dp[i][j][2] = dp[i - 1][j][1]

ans = sum(dp[-1][0]) + sum(dp[-1][1]) + sum(dp[-1][2])
print(ans % mod)
