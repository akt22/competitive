from collections import Counter

import sys
sys.setrecursionlimit(500000)


N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

dp = [[[-1] * (N + 2) for _ in range(N + 2)] for _ in range(N + 2)]


def rec(i, j, k):
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    if i == 0 and j == 0 and k == 0:
        return 0.0
    ret = 0.0
    if i > 0:
        ret += i * rec(i - 1, j, k)
    if j > 0:
        ret += j * rec(i + 1, j - 1, k)
    if k > 0:
        ret += k * rec(i, j + 1, k - 1)
    ret += N
    ret *= 1 / (i + j + k)
    dp[i][j][k] = ret
    return ret


print(rec(*[cnt[i] for i in range(1, 4)]))
