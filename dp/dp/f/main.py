s = input()
t = input()

ls, lt = len(s), len(t)

dp = [[0] * (lt + 1) for _ in range(ls + 1)]

for i in range(1, ls + 1):
    for j in range(1, lt + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])

ans = ""
while ls > 0 and lt > 0:
    if dp[ls][lt] == dp[ls - 1][lt]:
        ls -= 1
    elif dp[ls][lt] == dp[ls][lt - 1]:
        lt -= 1
    else:
        ls -= 1
        lt -= 1
        ans += s[ls]
print(ans[::-1])
