import sys
sys.setrecursionlimit(10**8)

m = int(input())
n = int(input())

ices = [list(map(int, input().split())) for _ in range(n)]

moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
ans = 0


def dfs(x, y, cnt):
    res = cnt
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and ices[ny][nx] == 1 and visited[ny][nx] != True:
            visited[ny][nx] = True
            res = max(res, dfs(nx, ny, cnt + 1))
            visited[ny][nx] = False
    return res

for y in range(n):
    for x in range(m):
        if ices[y][x] == 1:
            visited = [[False for i in range(m)] for i in range(n)]
            visited[y][x] = True
            cnt = dfs(x, y, 1)
            ans = max(cnt, ans)
print(ans)
