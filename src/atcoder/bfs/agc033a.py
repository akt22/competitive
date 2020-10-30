# from time import sleep

# def pp():
#     print("==========")
#     for y, row in enumerate(maze):
#         for x, p in enumerate(row):
#             if [x, y] in blacks:
#                 print("#", end="")
#             else:
#                 print(p, end="")
#         print()
#     print("==========")


from collections import deque

def main():
    used = [[True] * (W+2) for _ in range(H+2)]
    q = deque()
    for y, row in enumerate(maze):
        used[y+1][1:-1] = map(lambda _:_=="#", maze[y])
        for x, p in enumerate(row):
            if p == "#":
                q.append((x+1, y+1, 0))
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        r, c, k = q.popleft()
        for nx, ny in moves:
            nx, ny = r + nx, c + ny
            if not used[ny][nx]:
                q.append((nx, ny, k+1))
                used[ny][nx] = True
    print(k)

if __name__ == "__main__":
    H, W = map(int, input().strip().split(" "))
    maze = []
    for _ in range(H):
        maze.append(list(input().strip()))

    squares = H * W
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    main()
