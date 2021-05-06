N = int(input())
S = input()

dp = [[0] * 8 for _ in range(N + 1)]
dp[0][0] = 1

MOD = 10**9 + 7

for i in range(N):
    for j in range(8):
        if (S[i] == "a" and j == 0) \
            or (S[i] == "t" and j == 1)\
            or (S[i] == "c" and j == 2)\
            or (S[i] == "o" and j == 3)\
            or (S[i] == "d" and j == 4)\
            or (S[i] == "e" and j == 5)\
                or (S[i] == "r" and j == 6):
            dp[i + 1][j + 1] += dp[i][j] % MOD
        dp[i + 1][j] += dp[i][j] % MOD
print(dp[N][7] % MOD)
