N, M, Q = map(int, input().split())

trains = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    l, r = map(int, input().split())
    trains[l][r] += 1


queries = [list(map(int, input().split())) for _ in range(Q)]

acc = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        acc[i][j] = acc[i][j - 1] + trains[i][j]

for p, q in queries:
    ans = 0
    for i in range(p, q + 1):
        ans += acc[i][q] - acc[i][p - 1]
    print(ans)
