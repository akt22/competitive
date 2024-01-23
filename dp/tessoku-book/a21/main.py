N = int(input())
P, A = [0], [0]
for _ in range(N):
    p, a = list(map(int, input().split()))
    P.append(p)
    A.append(a)
P.append(0)
A.append(0)

dp = [[0] * (N + 1) for _ in range(N + 1)]

for length in range(N - 2, -1, -1):
    for l in range(1, N - length + 1):
        r = l + length
        score1 = A[l - 1] if (l - 1) <= P[l - 1] <= r else 0
        score2 = A[r + 1] if l <= P[r + 1] <= (r + 1) else 0

        if r == N:
            dp[l][r] = dp[l - 1][r] + score1
        elif l == 1:
            dp[l][r] = dp[l][r + 1] + score2
        else:
            dp[l][r] = max(dp[l - 1][r] + score1, dp[l][r + 1] + score2)

ans = 0
for row in dp:
    ans = max(ans, *row)
print(ans)
