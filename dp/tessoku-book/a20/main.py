S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(S) - 1][len(T) - 1])
