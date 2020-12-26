N = int(input())

colors = ["B", "W", "R"]


flag = [list(input()) for _ in range(5)]

INF = 10**9
dp = [[INF] * (4) for _ in range(N + 1)]
for j, color in enumerate(colors):
    cnt = 5
    for i in range(5):
        if flag[i][0] == color:
            cnt -= 1
    dp[0][j] = cnt

for i in range(1, N):
    for j, color in enumerate(colors):
        for k, color2 in enumerate(colors):
            if color == color2:
                continue
            cnt = 5
            for l in range(5):
                if flag[l][i] == color:
                    cnt -= 1
            dp[i][j] = min(dp[i][j], dp[i - 1][k] + cnt)

print(min(dp[N - 1]))
