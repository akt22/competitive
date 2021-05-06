from collections import Counter

N = int(input())

cnt = Counter(map(int, input().split(" ")))
dp = [[[-1 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]

for k in range(N + 1):
    for j in range(N + 1):
        if k + j > N:
            break
        for i in range(N + 1):
            c = i + j + k
            if c > N:
                break
            if c == 0:
                continue
            res = N
            if i > 0:
                res += dp[i - 1][j][k] * i
            if j > 0:
                res += dp[i + 1][j - 1][k] * j
            if k > 0:
                res += dp[i][j + 1][k - 1] * k
            res /= c
            dp[i][j][k] = res

print(dp[cnt[1]][cnt[2]][cnt[3]] + 1.0)
