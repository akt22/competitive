H, W = list(map(int, input().split()))
maze = [input() + "#" for _ in range(H)]
maze.append("#" * (W + 1))

MOD = 10**9 + 7

dp = [[0] * (W + 1) for _ in range(H + 1)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        # 今いる場所が '#'
        if dp[i][j] == 0:
            continue

        # 右への移動
        if maze[i + 1][j] == "#":  # 右隣が '#' なら0
            dp[i + 1][j] = 0
        else:  # そのマスへの初めての移動 & すでに移動しててdpに値が入ってる場合
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD

        # 下への移動
        if maze[i][j + 1] == "#":  # 下が '#' なら0
            dp[i][j + 1] = 0
        else:  # そのマスへの初めての移動 & すでに移動しててdpに値が入ってる場合
            dp[i][j + 1] += dp[i][j]
            dp[i][j + 1] %= MOD

print(dp[H - 1][W - 1])
