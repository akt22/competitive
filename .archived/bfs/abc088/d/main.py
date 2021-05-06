from collections import deque

H, W = map(int, input().split())
maze = []

for _ in range(H):
    maze.append(list(input()))


def pp():
    for y in range(H):
        for x in range(W):
            print(maze[y][x], end=" ")
        print()


moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
INF = 10**8
path = [[INF] * W for _ in range(H)]

q = deque()
q.append([0, 0])
path[0][0] = 0

while q:
    x, y = q.popleft()
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and maze[ny][nx] != "#" and path[ny][nx] == INF:
            q.append([nx, ny])
            path[ny][nx]  = path[y][x] + 1

if path[H - 1][W - 1] == INF:
    print(-1)
    exit()

blacks = 0
for l in maze:
    blacks += l.count("#")
print(H * W - blacks - path[H - 1][W - 1] - 1)
