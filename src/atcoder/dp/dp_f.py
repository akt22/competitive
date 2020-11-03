s = input()
t = input()

lenS = len(s)
lenT = len(t)

dp = [[0 for _ in range(lenT + 1)] for _ in range(lenS + 1)]

for i, si in enumerate(s):
    for j, tj in enumerate(t):
        if si == tj:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])

ans = ""
i, j = lenS, lenT
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans = s[i - 1] + ans
        i -= 1
        j -= 1
print(ans)
