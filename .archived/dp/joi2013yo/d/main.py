D, N = map(int, input().split())
degrees = [int(input()) for _ in range(D)]
clothes = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(D + 1)]

for j in range(N):
    low, high, _ = clothes[j]
    t = degrees[0]
    if low <= t <= high:
        dp[0][j] = 0


for i in range(1, D):
    t = degrees[i]
    for j, (low, high, f) in enumerate(clothes):
        if low <= t <= high:
            for k in range(N):
                if dp[i - 1][k] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(f - clothes[k][2]))
print(max(dp[D - 1]))
