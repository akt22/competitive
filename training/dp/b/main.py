N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

dp = [0] * (N + 1)
dp[0] = 0
dp[1] = abs(H[0] - H[1])
if N == 2:
    print(dp[1])
    exit()
if K > 1:
    dp[2] = min(dp[0] + abs(H[0] - H[2]), dp[1] + abs(H[1] - H[2]))
else:
    dp[2] = dp[1] + abs(H[1] - H[2])
for i in range(2, N - 1):
    for k in range(K):
        if i - k < 0:
            break
        if k == 0:
            dp[i + 1] = dp[i] + abs(H[i] - H[i + 1])
        else:
            dp[i + 1] = min(dp[i + 1], dp[i - k] + abs(H[i - k] - H[i + 1]))
print(dp[N - 1])
