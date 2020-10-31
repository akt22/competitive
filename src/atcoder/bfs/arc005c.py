from collections import deque
# from time import sleep

# def pp(visited):
#     print("==========")
#     for y, row in enumerate(maze):
#         for x, p in enumerate(row):
#             if visited[x][y] != INF and p == "#":
#                 print(visited[x][y], end="")
#             elif visited[x][y] != INF:
#                 print("*", end="")
#             else:
#                 print(p, end="")
#         print()
#     print("==========")


def main():
    q = deque()
    q.append([sx, sy, 0])
    visited[sx][sy] = 0

    while q:
        x, y, k = q.popleft()

        if x == gx and y == gy:
            print("YES")
            exit()

        nk = k + int(maze[y][x] == "#")

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (0 <= nx < W) and (0 <= ny < H) and visited[nx][ny] > nk and nk < 3:
                q.append([nx, ny, nk])
                visited[nx][ny] = nk

        # pp(visited)
        # sleep(0.2)

    print("NO")


if __name__ == "__main__":
    H, W = map(int, input().strip().split(" "))
    maze = []
    for _ in range(H):
        maze.append(list(input().strip()))

    sx, sy, gx, gy = 0, 0, 0, 0

    for y, row in enumerate(maze):
        for x, point in enumerate(row):
            if point == "s":
                sx, sy = x, y
            if point == "g":
                gx, gy = x, y

    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    INF = 10000000
    visited = [[INF] * H for _ in range(W)]
    main()
