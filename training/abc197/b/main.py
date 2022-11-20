H, W, X, Y = list(map(int, input().split()))

maze = [list(input()) for _ in range(H)]

X -= 1
Y -= 1

ans = 0
if maze[X][Y] == ".":
    ans += 1

for x in range(X + 1, H):
    if maze[x][Y] == "#":
        break
    ans += 1

for x in range(X - 1, -1, -1):
    if maze[x][Y] == "#":
        break
    ans += 1

for y in range(Y + 1, W):
    if maze[X][y] == "#":
        break
    ans += 1

for y in range(Y - 1, -1, -1):
    if maze[X][y] == "#":
        break
    ans += 1
print(ans)
