A, B = map(int, input().split(" "))
alist = list(map(int, input().split(" ")))
blist = list(map(int, input().split(" ")))

dp = [[0 for _ in range(B + 1)] for _ in range(A + 1)]

for i in reversed(range(A + 1)):
    for j in reversed(range(B + 1)):
        if i == A and j == B:
            continue
        if (i + j) % 2 == 0:
            if i == A:
                dp[i][j] = blist[j] + dp[i][j + 1]
            elif j == B:
                dp[i][j] = alist[i] + dp[i + 1][j]
            else:
                dp[i][j] = max(alist[i] + dp[i + 1][j], blist[j] + dp[i][j + 1])
        else:
            if i == A:
                dp[i][j] = dp[i][j + 1]
            elif j == B:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1])

print(dp[0][0])
