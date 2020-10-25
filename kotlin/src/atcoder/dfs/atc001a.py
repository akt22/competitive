import sys
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            sy, sx = i, j

def dfs(y, x):
    if not 0 <= y < h or not 0 <= x < w or c[y][x] == '#':
        return
    if c[y][x] == 'g':
        print('Yes')
        exit()

    c[y][x] = '#' 
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)

dfs(sy, sx)
print('No')
