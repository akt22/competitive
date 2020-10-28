def main():
    q = [[sx, sy]]
    d[sx][sy] = 0

    while len(q) != 0:
        x, y = q.pop(0)
        if x == gx and y == gy:
            break
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if (0 <= nx < C) and (0 <= ny < R) and maze[ny][nx] != "#" and d[ny][nx] == INF:
                q.append([nx, ny])
                d[ny][nx] = d[y][x] + 1

    print(d[gy][gx])


if __name__ == "__main__":
    INF = 10000000

    R, C = map(int, input().strip().split(" "))
    sy, sx = map(lambda x: int(x) - 1, input().strip().split(" "))
    gy, gx = map(lambda x: int(x) - 1, input().strip().split(" "))

    maze = []
    for _ in range(R):
        maze.append(list(input().strip()))

    d = [[INF] * C for _ in range(R)]
    main()
