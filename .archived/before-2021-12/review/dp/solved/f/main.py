S = input()
T = input()


dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for i, s in enumerate(S):
    for j, t in enumerate(T):
        if s == t:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])

ans = ""
i, j = len(S), len(T)
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans = S[i - 1] + ans
        i -= 1
        j -= 1
print(ans)
