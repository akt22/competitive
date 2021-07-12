s = input()
t = input()

ls = len(s)
lt = len(t)

dp = [[0] * (lt + 1) for _ in range(ls + 1)]

for i in range(ls):
    for j in range(lt):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])

ans = ""
i, j = ls, lt
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans += s[i - 1]
        i -= 1
        j -= 1
print(ans[::-1])
