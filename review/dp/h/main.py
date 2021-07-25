H, W = list(map(int, input().split()))
maze = []
for i in range(H):
    maze.append(list(input()))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[0] * W for _ in range(H)]
MOD = 10**9 + 7

dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i + 1 < H and maze[i + 1][j] == '.':
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
        if j + 1 < W and maze[i][j + 1] == ".":
            dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD
print(dp[H - 1][W - 1])
