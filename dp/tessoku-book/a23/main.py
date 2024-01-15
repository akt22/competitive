N, M = list(map(int, input().split()))
A = [[int(x) for x in input().split()] for _ in range(M)]

INF = 1 << 60
dp = [[INF] * (2**N) for _ in range(M + 1)]

dp[0][0] = 0

for i in range(1, M + 1):
    for j in range(1 << N):
        already = [None for _ in range(N)]
        for k in range(N):
            if (j // 2**k) % 2 == 0:
                already[k] = 0
            else:
                already[k] = 1
        v = 0
        for k in range(N):
            if already[k] == 1 or A[i - 1][k] == 1:
                v += 2**k

        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1)

print(dp[M][-1] if dp[M][-1] != INF else -1)
