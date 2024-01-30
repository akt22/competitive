N = int(input())
a, b, c = [0], [0], [0]

for _ in range(N):
    _a, _b, _c = list(map(int, input().split()))
    a.append(_a)
    b.append(_b)
    c.append(_c)

dp = [[0] * (3) for _ in range(N + 1)]
dp[1][0] = a[1]
dp[1][1] = b[1]
dp[1][2] = c[1]

for i in range(2, N + 1):
    dp[i][0] = max(dp[i - 1][1] + a[i], dp[i - 1][2] + a[i])
    dp[i][1] = max(dp[i - 1][0] + b[i], dp[i - 1][2] + b[i])
    dp[i][2] = max(dp[i - 1][0] + c[i], dp[i - 1][1] + c[i])

print(max(dp[N]))
