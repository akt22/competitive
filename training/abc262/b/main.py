
N, M = list(map(int, input().split()))

g = [[False] * N for _ in range(N)]
for _ in range(M):
    u, v = list(map(int, input().split()))
    g[u - 1][v - 1] = True
    g[v - 1][u - 1] = True

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if g[i][j] and g[j][k] and g[k][i]:
                ans += 1
print(ans)
