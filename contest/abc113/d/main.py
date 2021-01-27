H, W, K = map(int, input().split())

dp = [[0] * (W + 1) for _ in range(H + 1)]

MOD = 10**9 + 7

dp[0][0] = 1

for i in range(H):
    for j in range(W):
        for b in range(2**(W - 1)):
            is_valid = True
            for k in range(W - 2):
                if (b >> k) & 1 and (b >> (k + 1)) & 1:
                    is_valid = False
            if not is_valid:
                continue

            nj = j
            if (b >> j) & 1:
                nj += 1
            elif j > 0 and (b >> (j - 1)) & 1:
                nj -= 1

            dp[i + 1][nj] += dp[i][j]
            dp[i + 1][nj] %= MOD

print(dp[H][K - 1] % MOD)
