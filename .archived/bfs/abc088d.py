def main():
    q = [[sx, sy]]
    d[0][0] = 0
    while len(q) != 0:
        x, y = q.pop(0)
        if x == gx and y == gy:
            break
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (0 <= nx < W) and (0 <= ny < H) and maze[ny][nx] != "#" and d[ny][nx] == INF:
                q.append([nx, ny])
                d[ny][nx] = d[y][x] + 1

    if d[gy][gx] == INF:
        print(-1)
        exit(0)

    print(H*W - d[gy][gx] - black_count - 1)


if __name__ == "__main__":
    H, W = map(int, input().strip().split(" "))
    maze = []
    sx, sy, gx, gy = 0, 0, W-1, H-1
    INF = 10000000
    d = [[INF] * W for _ in range(H)]
    for _ in range(H):
        maze.append(list(input().strip()))

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    black_count = 0
    for r in maze:
        black_count += r.count("#")

    main()
