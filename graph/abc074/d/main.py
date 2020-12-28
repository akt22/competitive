N = int(input())

g = [[0] * N for _ in range(N)]
needed = [[True] * N for _ in range(N)]
for i in range(N):
    for j, cost in enumerate(map(int, input().split())):
        g[i][j] = cost

for k in range(N):
    for i in range(N):
        for j in range(N):
            if k == i or i == j or j == k:
                continue
            if g[i][j] > g[i][k] + g[k][j]:
                print(-1)
                exit()
            if g[i][j] == g[i][k] + g[k][j]:
                needed[i][j] = False

ans = 0
for i in range(N):
    for j in range(i + 1):
        if needed[i][j]:
            ans += g[i][j]
print(ans)
