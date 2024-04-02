N, A, B = list(map(int, input().split()))

dp = [False] * (N + 2)

for i in range(N + 1):
    if i - A >= 0 and not dp[i - A]:
        dp[i] = True
    elif i - B >= 0 and not dp[i - B]:
        dp[i] = True

print("First" if dp[N] else "Second")
