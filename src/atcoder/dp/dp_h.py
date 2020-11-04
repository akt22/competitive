H, W = map(int, input().split(" "))
maze = [list(input().strip()) for _ in range(H)]

p = 10**9 + 7

dp = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
dp[0][0] = 1


for i in range(H):
    for j in range(W):
        # print(f"{i=}, {j=}")
        if i + 1 < H and maze[i + 1][j] != "#":
            dp[i + 1][j] = dp[i][j]
            dp[i + 1][j] %= p
        if j + 1 < W and maze[i][j + 1] != "#":
            dp[i][j + 1] += dp[i][j]
            dp[i][j + 1] %= p

print(dp[H - 1][W - 1])
