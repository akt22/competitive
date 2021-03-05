
H, W, K = list(map(int, input().split()))
maze = []
for _ in range(H):
    maze.append(list(input()))

ans = 0
for r in range(2**H):
    for c in range(2**W):
        b = 0
        for i in range(H):
            for j in range(W):
                if (r >> i) & 1 and (c >> j) & 1:
                    if maze[i][j] == "#":
                        b += 1
        if b == K:
            ans += 1
print(ans)
