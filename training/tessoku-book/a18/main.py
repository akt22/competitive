N, S = list(map(int, input().split()))
A = list(map(int, input().split()))

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        # [j - A[i - 1]] < 0にならないように
        if j < A[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
print("Yes" if dp[N][S] else "No")
# print(*dp, sep="\n")
