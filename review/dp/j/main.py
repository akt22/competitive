from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

dp = [[[0.0] * (N + 2) for _ in range(N + 2)] for _ in range(N + 2)]


for k in range(N + 1):
    for j in range(N + 1 - k):
        for i in range(N + 1 - k - j):
            if i == j == k == 0:
                continue
            if i > 0:
                dp[i][j][k] += i * dp[i - 1][j][k]
            if j > 0:
                dp[i][j][k] += j * dp[i + 1][j - 1][k]
            if k > 0:
                dp[i][j][k] += k * dp[i][j + 1][k - 1]
            dp[i][j][k] += N
            dp[i][j][k] /= i + j + k
print(dp[cnt[1]][cnt[2]][cnt[3]])
