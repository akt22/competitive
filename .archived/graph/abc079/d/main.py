from collections import defaultdict, deque
H, W = map(int, input().split())

g = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j, cost in enumerate(map(int, input().split())):
        g[i][j] = cost

wall = [list(map(int, input().split())) for _ in range(H)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])


ans = 0
for row in wall:
    for elem in row:
        if elem == -1 or elem == 1:
            continue
        ans += g[elem][1]
print(ans)
