H, W = list(map(int, input().split()))
maze = [list(input()) for _ in range(H)]

MOD = 10**9 + 7

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if maze[i][j] == "#":
            continue
        l = dp[i][j - 1] if j - 1 < W and maze[i][j - 1] != "#" else 0
        t = dp[i - 1][j] if i - 1 < H and maze[i - 1][j] != "#" else 0
        dp[i][j] = max(dp[i][j], (l + t) % MOD)
print(dp[H - 1][W - 1])
