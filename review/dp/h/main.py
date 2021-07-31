H, W = list(map(int, input().split()))
maze = []
for i in range(H):
    maze.append(list(input()))


dp = [[0] * W for _ in range(H)]
for i in range(W):
    if maze[0][i] == '#':
        break
    dp[0][i] = 1
for j in range(H):
    if maze[j][0] == '#':
        break
    dp[j][0] = 1

MOD = 10**9 + 7

for i in range(1, H):
    for j in range(1, W):
        if maze[i][j] == '.':
            dp[i][j] = dp[i][j] + dp[i - 1][j] + dp[i][j - 1]
            dp[i][j] %= MOD
print(dp[H - 1][W - 1])
