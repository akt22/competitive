from time import sleep
from collections import deque

h, w, n = map(int, input().split())
maze = [list(input()) for _ in range(h)]

q = deque()
moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def pp(x, y):
    sleep(0.2)
    print("===================")
    for _y in range(h):
        for _x in range(w):
            if x == _x and y == _y:
                print("*", end=" ")
            else:
                print(maze[_y][_x], end=" ")
        print()
    print("===================")


def is_finished():
    for y in range(h):
        for x in range(w):
            if maze[y][x].isnumeric():
                return False
    return True


visited = [[False for _ in range(w)] for _ in range(h)]

for y in range(h):
    for x in range(w):
        if maze[y][x] == 'S':
            q.append([x, y, 1, 0])
            visited[y][x] = True
            break


while q:
    x, y, hp, cnt = q.popleft()
    # print(f"(x, y, hp): {x}, {y}, {hp}")
    # pp(x, y)

    if maze[y][x].isnumeric() and hp >= int(maze[y][x]):
        hp += 1
        maze[y][x] = "."
        visited = [[False for _ in range(w)] for _ in range(h)]
        q = deque()
        if is_finished():
            print(cnt)
            exit()

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] != "X" and visited[ny][nx] != True:
            q.append([nx, ny, hp, cnt + 1])
            visited[ny][nx] = True
