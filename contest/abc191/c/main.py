H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]


ans = 0
for y in range(H - 1):
    for x in range(W - 1):
        edge = [maze[y][x], maze[y + 1][x], maze[y][x + 1], maze[y + 1][x + 1]]
        c = edge.count("#")
        if c == 1 or c == 3:
            ans += 1
print(ans)
