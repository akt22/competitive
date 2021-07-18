import sys
sys.setrecursionlimit(10 ** 9)

H, W  = list(map(int, input().split()))
maze = []
for _ in range(H):
    maze.append(list(map(int, input().split())))

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dp = [[-1] * W for _ in range(H)]
MOD = 10**9 + 7


def rec(x, y):
    if dp[y][x] != -1:
        return dp[y][x]
    res = 1
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and maze[y][x] < maze[ny][nx]:
            res += rec(nx, ny)
    dp[y][x] = res % MOD
    return dp[y][x]


ans = 0
for y in range(H):
    for x in range(W):
        ans += rec(x, y)
        ans %= MOD
print(ans)
