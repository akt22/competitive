S = input()
L = len(S)

MOD = 10**9 + 7

dp = [[0] * (4) for _ in range(L + 1)]
dp[0][0] = 1
for i in range(L):
    for j in range(4):
        m = 3 if S[i] == "?" else 1
        dp[i + 1][j] += (m * dp[i][j] % MOD)
        if j == 0:
            continue
        if S[i] == "?" or S[i] == "ABC"[j - 1]:
            dp[i + 1][j] += (dp[i][j - 1] % MOD)
    # if S[i] == "?" or S[i] == "A":
    #     dp[i + 1][1] += (dp[i][0] % MOD)
    # if S[i] == "?" or S[i] == "B":
    #     dp[i + 1][2] += (dp[i][1] % MOD)
    # if S[i] == "?" or S[i] == "C":
    #     dp[i + 1][3] += (dp[i][2] % MOD)
# print(dp)
print(dp[L][3] % MOD)
