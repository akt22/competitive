N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

matches = dict(zip(range(1, 10), [2, 5, 5, 4, 5, 6, 3, 7, 6]))

dp = [-10**10] * (N + 10)
dp[0] = 0

for i in range(N + 1):
    for a in A:
        dp[i] = max(dp[i], dp[i - matches[a]] + 1)

ans = []
remain = N
for _ in range(dp[N], 0, -1):
    for a in A:
        if dp[remain] == dp[remain - matches[a]] + 1:
            ans.append(a)
            remain -= matches[a]
            break
print(*ans, sep="")
